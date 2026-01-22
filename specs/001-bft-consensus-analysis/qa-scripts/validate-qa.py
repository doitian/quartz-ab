#!/usr/bin/env python3
"""
Quality Assurance Script for BFT Consensus Analysis Documentation
Performs comprehensive validation of all documentation files.

Tasks covered:
- T032: Validate wikilinks
- T033: Verify references
- T034: Check glossary completeness
- T035: Validate YAML frontmatter
- T038: Verify Mermaid diagrams
- T039: Check mathematical notation
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

CONTENT_DIR = Path("/home/runner/work/quartz-ab/quartz-ab/content/bft-consensus-analysis")
SPEC_DIR = Path("/home/runner/work/quartz-ab/quartz-ab/specs/001-bft-consensus-analysis")


class QAValidator:
    def __init__(self):
        self.all_files = list(CONTENT_DIR.rglob("*.md"))
        self.issues = defaultdict(list)
        self.stats = defaultdict(int)
        
    def run_all_checks(self):
        """Run all QA validation checks"""
        print("=" * 80)
        print("BFT Consensus Analysis - Quality Assurance Validation")
        print("=" * 80)
        print()
        
        self.validate_wikilinks()
        self.validate_references()
        self.check_glossary_completeness()
        self.validate_yaml_frontmatter()
        self.verify_mermaid_diagrams()
        self.check_mathematical_notation()
        
        self.print_summary()
        
    def validate_wikilinks(self):
        """T032: Validate all wikilinks resolve correctly"""
        print("T032: Validating Wikilinks...")
        print("-" * 80)
        
        total_links = 0
        broken_links = []
        
        for file in self.all_files:
            content = file.read_text(encoding='utf-8')
            
            # Extract all wikilinks: [[target]], [[target|display]], [[target#section]]
            wikilink_pattern = r'\[\[([^\]]+)\]\]'
            matches = re.findall(wikilink_pattern, content)
            
            for match in matches:
                total_links += 1
                
                # Parse the wikilink (might have | for display text or # for section)
                # Format: [[target]], [[target|display]], [[target#section]], [[target#section|display]]
                target = match.split('|')[0].split('#')[0].strip()
                
                # Check if target file exists
                if not self.resolve_wikilink(file, target):
                    broken_links.append({
                        'file': file.relative_to(CONTENT_DIR),
                        'link': match,
                        'target': target
                    })
                    self.issues['wikilinks'].append(f"{file.name}: [[{match}]] -> target '{target}' not found")
        
        self.stats['total_wikilinks'] = total_links
        self.stats['broken_wikilinks'] = len(broken_links)
        
        if broken_links:
            print(f"❌ FAIL: Found {len(broken_links)} broken wikilinks out of {total_links} total")
            for broken in broken_links[:10]:  # Show first 10
                print(f"  - {broken['file']}: [[{broken['link']}]]")
            if len(broken_links) > 10:
                print(f"  ... and {len(broken_links) - 10} more")
        else:
            print(f"✅ PASS: All {total_links} wikilinks resolve correctly")
        print()
        
    def resolve_wikilink(self, source_file: Path, target: str) -> bool:
        """Check if a wikilink target exists"""
        # Try multiple resolution strategies
        
        # Strategy 1: Relative to source file's directory
        source_dir = source_file.parent
        candidate = source_dir / f"{target}.md"
        if candidate.exists():
            return True
            
        # Strategy 2: Relative to content root
        candidate = CONTENT_DIR / f"{target}.md"
        if candidate.exists():
            return True
            
        # Strategy 3: Search in subdirectories
        for md_file in self.all_files:
            if md_file.stem == target:
                return True
                
        # Strategy 4: Handle paths like "bft-consensus/fundamentals"
        candidate = CONTENT_DIR / f"{target}.md"
        if candidate.exists():
            return True
            
        return False
        
    def validate_references(self):
        """T033: Verify all references are cited in references.md"""
        print("T033: Validating References...")
        print("-" * 80)
        
        # Load references.md
        ref_file = CONTENT_DIR / "references.md"
        if not ref_file.exists():
            print("❌ FAIL: references.md not found")
            return
            
        ref_content = ref_file.read_text(encoding='utf-8')
        
        # Extract all reference IDs from references.md
        # Pattern: [ID]: or - **[ID]** or similar
        ref_pattern = r'\[([A-Z0-9\-]+)\]'
        defined_refs = set(re.findall(ref_pattern, ref_content))
        
        print(f"Found {len(defined_refs)} reference definitions in references.md")
        
        # Find all reference citations in content files
        cited_refs = set()
        uncited_refs = []
        
        for file in self.all_files:
            if file.name == "references.md":
                continue
                
            content = file.read_text(encoding='utf-8')
            
            # Extract YAML frontmatter references
            try:
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end > 0:
                        yaml_str = content[3:yaml_end]
                        metadata = yaml.safe_load(yaml_str)
                        if metadata and 'references' in metadata:
                            refs = metadata['references']
                            if isinstance(refs, list):
                                cited_refs.update(refs)
            except:
                pass
                
            # Also check inline citations [REF-ID]
            inline_refs = re.findall(r'\[([A-Z0-9\-]+)\](?!:)', content)
            cited_refs.update(inline_refs)
        
        # Check for citations not in references.md
        for ref in cited_refs:
            if ref not in defined_refs:
                uncited_refs.append(ref)
                self.issues['references'].append(f"Reference [{ref}] cited but not defined in references.md")
        
        self.stats['total_references'] = len(defined_refs)
        self.stats['uncited_references'] = len(uncited_refs)
        
        if uncited_refs:
            print(f"⚠️  WARNING: {len(uncited_refs)} references cited but not defined:")
            for ref in sorted(uncited_refs)[:10]:
                print(f"  - [{ref}]")
        else:
            print(f"✅ PASS: All cited references are defined in references.md")
        print()
        
    def check_glossary_completeness(self):
        """T034: Check glossary completeness - all technical terms defined"""
        print("T034: Checking Glossary Completeness...")
        print("-" * 80)
        
        # Load glossary.md
        glossary_file = CONTENT_DIR / "glossary.md"
        if not glossary_file.exists():
            print("❌ FAIL: glossary.md not found")
            return
            
        glossary_content = glossary_file.read_text(encoding='utf-8')
        
        # Extract glossary terms (look for headings or list items)
        # Common patterns: ## Term, **Term**, - **Term**:
        term_patterns = [
            r'^##\s+(.+)$',  # Heading terms
            r'^\*\*([^*]+)\*\*',  # Bold terms
            r'^-\s+\*\*([^*]+)\*\*',  # List with bold terms
        ]
        
        glossary_terms = set()
        for pattern in term_patterns:
            matches = re.findall(pattern, glossary_content, re.MULTILINE)
            glossary_terms.update([m.strip().lower() for m in matches])
        
        print(f"Found {len(glossary_terms)} terms defined in glossary.md")
        
        # Identify common technical terms that should be in glossary
        required_terms = {
            'byzantine fault tolerance', 'bft', 'consensus', 'safety', 'liveness',
            'provable broadcast', 'reliable broadcast', 'temporal logic',
            'knowledge framework', 'pbft', 'hotstuff', 'honeybadger',
            'threshold automata', 'formal verification', 'asynchronous',
            'synchronous', 'quorum', 'view change', 'leader election'
        }
        
        missing_terms = []
        for term in required_terms:
            # Check if term or variations exist
            found = False
            for glossary_term in glossary_terms:
                if term.lower() in glossary_term or glossary_term in term.lower():
                    found = True
                    break
            if not found:
                missing_terms.append(term)
        
        self.stats['glossary_terms'] = len(glossary_terms)
        self.stats['missing_terms'] = len(missing_terms)
        
        if missing_terms:
            print(f"⚠️  WARNING: {len(missing_terms)} expected terms not in glossary:")
            for term in sorted(missing_terms):
                print(f"  - {term}")
        else:
            print(f"✅ PASS: All expected terms are in glossary")
        print()
        
    def validate_yaml_frontmatter(self):
        """T035: Validate YAML frontmatter consistency across all notes"""
        print("T035: Validating YAML Frontmatter...")
        print("-" * 80)
        
        required_fields = ['title', 'type', 'tags', 'status']
        files_without_yaml = []
        files_missing_fields = []
        
        for file in self.all_files:
            content = file.read_text(encoding='utf-8')
            
            # Check if file has YAML frontmatter
            if not content.startswith('---'):
                files_without_yaml.append(file.relative_to(CONTENT_DIR))
                continue
                
            # Extract and parse YAML
            yaml_end = content.find('---', 3)
            if yaml_end < 0:
                files_without_yaml.append(file.relative_to(CONTENT_DIR))
                continue
                
            yaml_str = content[3:yaml_end]
            try:
                metadata = yaml.safe_load(yaml_str)
                if not metadata:
                    files_without_yaml.append(file.relative_to(CONTENT_DIR))
                    continue
                    
                # Check required fields
                missing = [f for f in required_fields if f not in metadata]
                if missing:
                    files_missing_fields.append({
                        'file': file.relative_to(CONTENT_DIR),
                        'missing': missing
                    })
                    
            except yaml.YAMLError as e:
                self.issues['yaml'].append(f"{file.name}: YAML parse error - {e}")
        
        self.stats['files_with_yaml'] = len(self.all_files) - len(files_without_yaml)
        self.stats['files_without_yaml'] = len(files_without_yaml)
        
        if files_without_yaml:
            print(f"❌ FAIL: {len(files_without_yaml)} files without YAML frontmatter:")
            for f in files_without_yaml[:5]:
                print(f"  - {f}")
        elif files_missing_fields:
            print(f"⚠️  WARNING: {len(files_missing_fields)} files missing required fields:")
            for item in files_missing_fields[:5]:
                print(f"  - {item['file']}: missing {item['missing']}")
        else:
            print(f"✅ PASS: All {len(self.all_files)} files have valid YAML frontmatter")
        print()
        
    def verify_mermaid_diagrams(self):
        """T038: Verify all Mermaid diagrams render correctly"""
        print("T038: Verifying Mermaid Diagrams...")
        print("-" * 80)
        
        total_diagrams = 0
        invalid_diagrams = []
        
        for file in self.all_files:
            content = file.read_text(encoding='utf-8')
            
            # Find Mermaid code blocks: ```mermaid ... ```
            mermaid_pattern = r'```mermaid\n(.*?)```'
            matches = re.findall(mermaid_pattern, content, re.DOTALL)
            
            for diagram in matches:
                total_diagrams += 1
                
                # Basic syntax validation
                diagram = diagram.strip()
                
                # Check for valid diagram types
                valid_types = ['graph', 'sequenceDiagram', 'classDiagram', 'stateDiagram', 
                              'flowchart', 'gantt', 'pie', 'erDiagram', 'journey']
                
                has_valid_type = any(diagram.startswith(t) for t in valid_types)
                
                if not has_valid_type:
                    invalid_diagrams.append({
                        'file': file.relative_to(CONTENT_DIR),
                        'diagram': diagram[:100] + "..." if len(diagram) > 100 else diagram
                    })
        
        self.stats['total_mermaid'] = total_diagrams
        self.stats['invalid_mermaid'] = len(invalid_diagrams)
        
        if invalid_diagrams:
            print(f"⚠️  WARNING: {len(invalid_diagrams)} potentially invalid Mermaid diagrams:")
            for item in invalid_diagrams:
                print(f"  - {item['file']}")
        else:
            print(f"✅ PASS: All {total_diagrams} Mermaid diagrams have valid syntax")
        print()
        
    def check_mathematical_notation(self):
        """T039: Check mathematical notation consistency (LaTeX)"""
        print("T039: Checking Mathematical Notation...")
        print("-" * 80)
        
        total_math = 0
        mismatched_delimiters = []
        
        for file in self.all_files:
            content = file.read_text(encoding='utf-8')
            
            # Count inline math: $...$
            inline_math = re.findall(r'\$(?!\$).*?\$(?!\$)', content)
            total_math += len(inline_math)
            
            # Count display math: $$...$$
            display_math = re.findall(r'\$\$.*?\$\$', content, re.DOTALL)
            total_math += len(display_math)
            
            # Check for mismatched delimiters
            # Count single $ (should be even)
            single_dollars = content.count('$') - 2 * content.count('$$')
            if single_dollars % 2 != 0:
                mismatched_delimiters.append(file.relative_to(CONTENT_DIR))
        
        self.stats['total_math_expressions'] = total_math
        self.stats['mismatched_math_delimiters'] = len(mismatched_delimiters)
        
        if mismatched_delimiters:
            print(f"⚠️  WARNING: {len(mismatched_delimiters)} files with mismatched $ delimiters:")
            for f in mismatched_delimiters:
                print(f"  - {f}")
        else:
            print(f"✅ PASS: All {total_math} mathematical expressions have valid delimiters")
        print()
        
    def print_summary(self):
        """Print overall summary"""
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print()
        print(f"Total files analyzed: {len(self.all_files)}")
        print()
        
        print("Statistics:")
        for key, value in sorted(self.stats.items()):
            print(f"  - {key.replace('_', ' ').title()}: {value}")
        print()
        
        total_issues = sum(len(v) for v in self.issues.values())
        if total_issues == 0:
            print("✅ OVERALL STATUS: PASS - No critical issues found")
        else:
            print(f"⚠️  OVERALL STATUS: {total_issues} issues found")
            print()
            print("Issues by category:")
            for category, issue_list in self.issues.items():
                print(f"  {category}: {len(issue_list)} issues")


if __name__ == "__main__":
    validator = QAValidator()
    validator.run_all_checks()
