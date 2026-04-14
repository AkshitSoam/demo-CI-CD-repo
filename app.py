from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Akshit Anime GKE App</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, Helvetica, sans-serif;
                background: linear-gradient(-45deg, #0f172a, #1e1b4b, #3b0764, #7f1d1d);
                background-size: 400% 400%;
                animation: gradientMove 12s ease infinite;
                color: white;
                min-height: 100vh;
                overflow: hidden;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
            }

            @keyframes gradientMove {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .particles {
                position: absolute;
                width: 100%;
                height: 100%;
                overflow: hidden;
                top: 0;
                left: 0;
                z-index: 0;
            }

            .particle {
                position: absolute;
                bottom: -20px;
                width: 8px;
                height: 8px;
                background: rgba(255, 255, 255, 0.7);
                border-radius: 50%;
                animation: floatUp linear infinite;
                box-shadow: 0 0 10px rgba(255,255,255,0.8);
            }

            @keyframes floatUp {
                0% {
                    transform: translateY(0) scale(1);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                100% {
                    transform: translateY(-110vh) scale(1.8);
                    opacity: 0;
                }
            }

            .card {
                position: relative;
                z-index: 1;
                width: min(900px, 92%);
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.18);
                backdrop-filter: blur(14px);
                -webkit-backdrop-filter: blur(14px);
                border-radius: 24px;
                padding: 40px 30px;
                text-align: center;
                box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35);
                animation: fadeInUp 1.1s ease;
            }

            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            .badge {
                display: inline-block;
                padding: 8px 16px;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.12);
                border: 1px solid rgba(255, 255, 255, 0.2);
                font-size: 14px;
                letter-spacing: 1px;
                margin-bottom: 18px;
                animation: pulse 2.5s infinite;
            }

            @keyframes pulse {
                0%, 100% { transform: scale(1); opacity: 0.95; }
                50% { transform: scale(1.05); opacity: 1; }
            }

            h1 {
                font-size: clamp(2.2rem, 5vw, 4.4rem);
                line-height: 1.1;
                margin-bottom: 14px;
                text-shadow: 0 0 12px rgba(255,255,255,0.35);
            }

            .gradient-text {
                background: linear-gradient(90deg, #f9a8d4, #c4b5fd, #93c5fd, #fca5a5);
                background-size: 300% auto;
                color: transparent;
                -webkit-background-clip: text;
                background-clip: text;
                animation: shine 5s linear infinite;
            }

            @keyframes shine {
                to { background-position: 300% center; }
            }

            .subtitle {
                font-size: 1.15rem;
                color: #e5e7eb;
                margin-bottom: 18px;
                min-height: 30px;
            }

            .description {
                max-width: 720px;
                margin: 0 auto 28px;
                font-size: 1rem;
                line-height: 1.8;
                color: #dbeafe;
            }

            .stats {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
                gap: 16px;
                margin: 30px 0;
            }

            .stat-box {
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255,255,255,0.14);
                border-radius: 18px;
                padding: 18px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }

            .stat-box:hover {
                transform: translateY(-6px) scale(1.02);
                box-shadow: 0 10px 24px rgba(0,0,0,0.25);
            }

            .stat-title {
                font-size: 0.9rem;
                color: #cbd5e1;
                margin-bottom: 8px;
            }

            .stat-value {
                font-size: 1.3rem;
                font-weight: bold;
                color: #ffffff;
            }

            .buttons {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 14px;
                margin-top: 10px;
            }

            .btn {
                text-decoration: none;
                color: white;
                padding: 12px 22px;
                border-radius: 999px;
                font-weight: bold;
                border: 1px solid rgba(255,255,255,0.25);
                background: rgba(255,255,255,0.12);
                transition: all 0.3s ease;
                box-shadow: 0 8px 18px rgba(0,0,0,0.2);
            }

            .btn:hover {
                transform: translateY(-3px) scale(1.04);
                background: rgba(255,255,255,0.2);
            }

            .footer {
                margin-top: 28px;
                font-size: 0.92rem;
                color: #d1d5db;
                opacity: 0.9;
            }

            .glow-ring {
                position: absolute;
                width: 420px;
                height: 420px;
                border-radius: 50%;
                background: radial-gradient(circle, rgba(255,255,255,0.18), transparent 60%);
                filter: blur(12px);
                z-index: 0;
                animation: spin 18s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg) scale(1); }
                50% { transform: rotate(180deg) scale(1.08); }
                100% { transform: rotate(360deg) scale(1); }
            }

            @media (max-width: 600px) {
                .card {
                    padding: 28px 18px;
                }

                .description {
                    font-size: 0.95rem;
                }
            }
        </style>
    </head>
    <body>
        <div class="particles" id="particles"></div>
        <div class="glow-ring"></div>

        <div class="card">
            <div class="badge">⚡ Deployed on GKE • Flask • Anime-Inspired UI</div>

            <h1>
                Hello GKE,
                <span class="gradient-text">I am Akshit Soam 🚀</span>
            </h1>

            <div class="subtitle" id="typewriter"></div>

            <p class="description">
                Welcome to my animated cloud-powered web app. This page is styled with a
                high-energy anime-inspired aesthetic — glowing visuals, motion effects,
                and a heroic launch-screen vibe — all running with plain Flask, HTML,
                CSS, and JavaScript only.
            </p>

            <div class="stats">
                <div class="stat-box">
                    <div class="stat-title">Deployment Platform</div>
                    <div class="stat-value">Google Kubernetes Engine</div>
                </div>
                <div class="stat-box">
                    <div class="stat-title">Backend</div>
                    <div class="stat-value">Python Flask</div>
                </div>
                <div class="stat-box">
                    <div class="stat-title">Theme Mode</div>
                    <div class="stat-value">Anime Energy</div>
                </div>
                <div class="stat-box">
                    <div class="stat-title">Status</div>
                    <div class="stat-value">Online ✅</div>
                </div>
            </div>

            <div class="buttons">
                <a class="btn" href="/">🏠 Home</a>
                <a class="btn" href="/health">💚 Health Check</a>
            </div>

            <div class="footer">
                “Powering up code, cloud, and creativity — one deployment at a time.”
            </div>
        </div>

        <script>
            const text = "Unleashing cloud power with style, speed, and a battle-ready spirit.";
            const target = document.getElementById("typewriter");
            let i = 0;

            function typeWriter() {
                if (i < text.length) {
                    target.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 45);
                }
            }
            typeWriter();

            const particles = document.getElementById("particles");
            for (let i = 0; i < 35; i++) {
                const p = document.createElement("div");
                p.className = "particle";
                p.style.left = Math.random() * 100 + "vw";
                p.style.animationDuration = (5 + Math.random() * 8) + "s";
                p.style.animationDelay = (Math.random() * 5) + "s";
                p.style.width = p.style.height = (4 + Math.random() * 8) + "px";
                particles.appendChild(p);
            }
        </script>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)