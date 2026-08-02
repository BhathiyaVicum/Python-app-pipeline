from flask import Flask
import os
import datetime
import socket
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DevOps Pipeline Demo</title>
            <style>
                /* ===== RESET & BASE ===== */
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}

                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    background: #0a0e1a;
                    color: #e0e6ed;
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                    background-image:
                        radial-gradient(ellipse at 10% 20%, rgba(100, 80, 255, 0.08) 0%, transparent 50%),
                        radial-gradient(ellipse at 90% 80%, rgba(0, 200, 255, 0.06) 0%, transparent 50%);
                }}

                /* ===== GLASS CARD ===== */
                .container {{
                    background: rgba(20, 28, 48, 0.85);
                    backdrop-filter: blur(20px);
                    -webkit-backdrop-filter: blur(20px);
                    border-radius: 24px;
                    padding: 50px 60px;
                    max-width: 820px;
                    width: 100%;
                    border: 1px solid rgba(255, 255, 255, 0.06);
                    box-shadow:
                        0 25px 60px rgba(0, 0, 0, 0.6),
                        inset 0 1px 0 rgba(255, 255, 255, 0.05);
                    transition: transform 0.3s ease;
                }}

                .container:hover {{
                    transform: translateY(-2px);
                }}

                /* ===== HEADER ===== */
                .header {{
                    text-align: center;
                    margin-bottom: 35px;
                }}

                .logo {{
                    font-size: 48px;
                    margin-bottom: 10px;
                    display: block;
                }}

                h1 {{
                    font-size: 32px;
                    font-weight: 700;
                    background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                    letter-spacing: -0.5px;
                }}

                .subtitle {{
                    font-size: 16px;
                    color: #94a3b8;
                    margin-top: 8px;
                    font-weight: 400;
                    letter-spacing: 0.3px;
                }}

                .subtitle strong {{
                    color: #e2e8f0;
                    font-weight: 600;
                }}

                /* ===== STATUS BADGE ===== */
                .badge-container {{
                    display: flex;
                    justify-content: center;
                    gap: 12px;
                    flex-wrap: wrap;
                    margin: 20px 0 28px 0;
                }}

                .badge {{
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    padding: 8px 20px;
                    border-radius: 100px;
                    font-size: 13px;
                    font-weight: 600;
                    letter-spacing: 0.3px;
                    text-transform: uppercase;
                }}

                .badge-success {{
                    background: rgba(52, 211, 153, 0.15);
                    color: #34d399;
                    border: 1px solid rgba(52, 211, 153, 0.2);
                }}

                .badge-success .dot {{
                    background: #34d399;
                    box-shadow: 0 0 12px rgba(52, 211, 153, 0.4);
                }}

                .badge-info {{
                    background: rgba(96, 165, 250, 0.12);
                    color: #60a5fa;
                    border: 1px solid rgba(96, 165, 250, 0.15);
                }}

                .dot {{
                    display: inline-block;
                    width: 8px;
                    height: 8px;
                    border-radius: 50%;
                    animation: pulse-dot 2s ease-in-out infinite;
                }}

                @keyframes pulse-dot {{
                    0%, 100% {{ opacity: 1; transform: scale(1); }}
                    50% {{ opacity: 0.4; transform: scale(0.85); }}
                }}

                /* ===== INFO GRID ===== */
                .info-grid {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 12px;
                    margin: 24px 0 28px 0;
                }}

                .info-item {{
                    background: rgba(255, 255, 255, 0.03);
                    border-radius: 12px;
                    padding: 16px 20px;
                    border: 1px solid rgba(255, 255, 255, 0.04);
                    transition: all 0.2s ease;
                }}

                .info-item:hover {{
                    background: rgba(255, 255, 255, 0.06);
                    border-color: rgba(255, 255, 255, 0.08);
                }}

                .info-label {{
                    font-size: 11px;
                    text-transform: uppercase;
                    letter-spacing: 0.8px;
                    color: #64748b;
                    font-weight: 600;
                    margin-bottom: 4px;
                }}

                .info-value {{
                    font-size: 14px;
                    font-weight: 500;
                    color: #e2e8f0;
                    word-break: break-all;
                    font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
                }}

                .info-value .highlight {{
                    color: #60a5fa;
                }}

                /* ===== DIVIDER ===== */
                .divider {{
                    border: none;
                    height: 1px;
                    background: linear-gradient(to right, transparent, rgba(255,255,255,0.06), transparent);
                    margin: 8px 0 20px 0;
                }}

                /* ===== FOOTER ===== */
                .footer {{
                    text-align: center;
                    color: #475569;
                    font-size: 13px;
                    line-height: 1.8;
                    padding-top: 4px;
                }}

                .footer a {{
                    color: #60a5fa;
                    text-decoration: none;
                    transition: color 0.2s ease;
                }}

                .footer a:hover {{
                    color: #93c5fd;
                    text-decoration: underline;
                }}

                .tech-stack {{
                    display: flex;
                    justify-content: center;
                    gap: 16px;
                    flex-wrap: wrap;
                    margin-top: 12px;
                }}

                .tech-tag {{
                    background: rgba(255, 255, 255, 0.04);
                    padding: 4px 14px;
                    border-radius: 100px;
                    font-size: 12px;
                    color: #94a3b8;
                    border: 1px solid rgba(255, 255, 255, 0.04);
                    font-weight: 500;
                }}

                .tech-tag:hover {{
                    background: rgba(255, 255, 255, 0.08);
                    color: #e2e8f0;
                }}

                /* ===== RESPONSIVE ===== */
                @media (max-width: 640px) {{
                    .container {{
                        padding: 30px 20px;
                    }}
                    .info-grid {{
                        grid-template-columns: 1fr;
                    }}
                    h1 {{
                        font-size: 26px;
                    }}
                    .logo {{
                        font-size: 36px;
                    }}
                    .badge-container {{
                        flex-direction: column;
                        align-items: center;
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="container">

                <!-- ===== HEADER ===== -->
                <div class="header">
                    <span class="logo">⚡</span>
                    <h1>Deployment Active</h1>
                    <p class="subtitle">
                        Deployed via <strong>Jenkins</strong> ·
                        <strong>Terraform</strong> ·
                        <strong>Docker</strong>
                    </p>
                </div>

                <!-- ===== BADGES ===== -->
                <div class="badge-container">
                    <span class="badge badge-success">
                        <span class="dot"></span> Operational
                    </span>
                    <span class="badge badge-info">
                        🚀 Jenkins Manual Build
                    </span>
                </div>

                <!-- ===== INFO GRID ===== -->
                <div class="info-grid">
                    <div class="info-item">
                        <div class="info-label">🕐 Deployment Time</div>
                        <div class="info-value">{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">🖥️ Container ID</div>
                        <div class="info-value"><span class="highlight">{os.popen('hostname').read().strip()}</span></div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">📦 Image</div>
                        <div class="info-value">bhathiyavi/python-app-2:<span class="highlight">v1</span></div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">🌍 Region</div>
                        <div class="info-value"><span class="highlight">us-east-1</span></div>
                    </div>
                </div>

                <hr class="divider">

                <!-- ===== FOOTER ===== -->
                <div class="footer">
                    <div class="tech-stack">
                        <span class="tech-tag">⚙️ Jenkins</span>
                        <span class="tech-tag">🏗️ Terraform</span>
                        <span class="tech-tag">🐳 Docker</span>
                        <span class="tech-tag">☁️ AWS</span>
                        <span class="tech-tag">🐍 Flask</span>
                    </div>
                </div>

            </div>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "uptime": os.popen('ps -o etime= -p 1').read().strip()
    }

@app.route('/info')
def info():
    return {
        "application": "python-app-2",
        "version": "v1",
        "container_id": os.popen('hostname').read().strip(),
        "deployment_time": datetime.datetime.now().isoformat(),
        "pipeline_trigger": "Jenkins Manual Build",
        "status": "running",
        "region": "us-east-1",
        "platform": platform.platform(),
        "python_version": platform.python_version()
    }

@app.route('/metrics')
def metrics():
    return {
        "cpu_usage": os.popen("top -bn1 | head -5 | awk '/Cpu/ {print $2}'").read().strip() + "%",
        "memory_usage": os.popen("free -m | awk '/Mem/ {print $3\"/\"$2\" MB\"}'").read().strip(),
        "uptime": os.popen("uptime -p").read().strip()
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)