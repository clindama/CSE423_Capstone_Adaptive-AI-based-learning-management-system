"""
Master Test Runner
Executes all test scripts and generates a comprehensive test report
"""

import subprocess
import sys
import os
from datetime import datetime
import json

# Test configurations
TESTS = [
    {
        'id': 'TEST-01',
        'name': 'Content Generation',
        'script': 'test_content_generation.py',
        'description': 'Verify AI generates unique instructional content based on user profiles',
        'requirement': 'AI Tutor must generate personalized instructional content'
    },
    {
        'id': 'TEST-02',
        'name': 'Problem Generation',
        'script': 'test_problem_generation.py',
        'description': 'Verify AI generates personalized practice problems based on user profiles',
        'requirement': 'AI Tutor must generate personalized practice problems'
    },
    {
        'id': 'TEST-03',
        'name': 'User Data Tracking',
        'script': 'test_user_data_tracking.py',
        'description': 'Verify user progress and practice attempts are correctly stored',
        'requirement': 'System must track and persist user progress and performance data'
    },
    {
        'id': 'TEST-04',
        'name': 'User Profile Update',
        'script': 'test_user_profile_update.py',
        'description': 'Verify AI updates user profiles with performance notes over time',
        'requirement': 'AI Tutor must maintain and update student profiles based on performance'
    },
    {
        'id': 'TEST-05',
        'name': 'AI Feedback',
        'script': 'test_ai_feedback.py',
        'description': 'Verify AI provides meaningful feedback on student answers',
        'requirement': 'AI Tutor must provide constructive feedback on student responses'
    }
]

def run_test(test_info):
    """Run a single test and return results"""
    print(f"\n{'='*80}")
    print(f"Running {test_info['id']}: {test_info['name']}")
    print(f"{'='*80}")
    
    script_path = os.path.join(os.path.dirname(__file__), test_info['script'])
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        return {
            'test_id': test_info['id'],
            'name': test_info['name'],
            'script': test_info['script'],
            'description': test_info['description'],
            'requirement': test_info['requirement'],
            'passed': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr,
            'return_code': result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            'test_id': test_info['id'],
            'name': test_info['name'],
            'script': test_info['script'],
            'description': test_info['description'],
            'requirement': test_info['requirement'],
            'passed': False,
            'output': '',
            'error': 'Test timed out after 120 seconds',
            'return_code': -1
        }
    except Exception as e:
        return {
            'test_id': test_info['id'],
            'name': test_info['name'],
            'script': test_info['script'],
            'description': test_info['description'],
            'requirement': test_info['requirement'],
            'passed': False,
            'output': '',
            'error': str(e),
            'return_code': -1
        }

def generate_report(results):
    """Generate a comprehensive test report"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = []
    report.append("=" * 80)
    report.append("COMPREHENSIVE TEST REPORT")
    report.append("Adaptive AI-Based Learning Management System")
    report.append("=" * 80)
    report.append(f"Test Execution Date: {timestamp}")
    report.append(f"Total Tests: {len(results)}")
    report.append(f"Tests Passed: {sum(1 for r in results if r['passed'])}")
    report.append(f"Tests Failed: {sum(1 for r in results if not r['passed'])}")
    report.append("=" * 80)
    
    # Summary table
    report.append("\nTEST SUMMARY")
    report.append("-" * 80)
    report.append(f"{'Test ID':<12} {'Test Name':<30} {'Status':<10}")
    report.append("-" * 80)
    
    for result in results:
        status = "✅ PASS" if result['passed'] else "❌ FAIL"
        report.append(f"{result['test_id']:<12} {result['name']:<30} {status:<10}")
    
    report.append("-" * 80)
    
    # Detailed results
    report.append("\n\nDETAILED TEST RESULTS")
    report.append("=" * 80)
    
    for result in results:
        report.append(f"\n{result['test_id']}: {result['name']}")
        report.append("-" * 80)
        report.append(f"Description: {result['description']}")
        report.append(f"Requirement: {result['requirement']}")
        report.append(f"Status: {'PASSED ✅' if result['passed'] else 'FAILED ❌'}")
        report.append(f"Return Code: {result['return_code']}")
        
        if result['output']:
            report.append("\nTest Output:")
            report.append(result['output'])
        
        if result['error']:
            report.append("\nErrors:")
            report.append(result['error'])
        
        report.append("\n" + "=" * 80)
    
    return "\n".join(report)

def main():
    """Main test execution function"""
    print("=" * 80)
    print("ADAPTIVE AI LMS - COMPREHENSIVE TEST SUITE")
    print("=" * 80)
    print(f"\nExecuting {len(TESTS)} tests...")
    
    results = []
    
    for test_info in TESTS:
        result = run_test(test_info)
        results.append(result)
        
        # Print immediate result
        status = "✅ PASSED" if result['passed'] else "❌ FAILED"
        print(f"\n{result['test_id']}: {status}")
    
    # Generate and save report
    report = generate_report(results)
    
    # Save to file
    report_filename = f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    report_path = os.path.join(os.path.dirname(__file__), report_filename)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n\n{'='*80}")
    print(f"Test report saved to: {report_filename}")
    print(f"{'='*80}")
    
    # Print summary
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    
    print(f"\nFINAL RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ ALL TESTS PASSED!")
        return 0
    else:
        print(f"❌ {total - passed} test(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())

