#!/usr/bin/env python3
"""
Simple test to verify pywebview installation works correctly.
Run this to make sure everything is set up properly.
"""

import webview

def create_test_window():
    """Create a simple test window to verify pywebview works"""
    
    # Simple HTML content for testing
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>OmniQueue - Test</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                margin: 0;
                padding: 50px;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 20px;
            }
            .success {
                background: rgba(0, 255, 0, 0.2);
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎵 OmniQueue</h1>
            <div class="success">
                <h2>✅ pywebview is working!</h2>
                <p>Your development environment is ready.</p>
                <p>Close this window to continue.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Create the window
    webview.create_window(
        title='OmniQueue - Test',
        html=html_content,
        width=800,
        height=600,
        resizable=True
    )

if __name__ == '__main__':
    print("Testing pywebview installation...")
    print("A window should open. Close it to finish the test.")
    
    create_test_window()
    webview.start(debug=True)
    
    print("Test completed successfully! ✅")
