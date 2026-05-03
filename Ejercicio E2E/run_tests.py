# Test execution script
import subprocess
import sys
import os

def run_tests():
    """Run the E2E tests"""
    
    print("🚀 Starting E2E Test Execution...")
    print("=" * 50)
    
    # Create reports directory if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    try:
        # Run pytest with HTML report
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_purchase_flow.py",
            "-v",
            "--html=reports/test_report.html",
            "--self-contained-html"
        ], capture_output=True, text=True)
        
        print("STDOUT:")
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ All tests passed!")
        else:
            print("❌ Some tests failed!")
            
        print(f"\n📊 Test report generated: reports/test_report.html")
        
    except Exception as e:
        print(f"❌ Error running tests: {str(e)}")

if __name__ == "__main__":
    run_tests()
