import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Ashutosh Dubey | Portfolio", layout="wide")

resume_link = "https://ibb.co/TMsJmcjq"

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ashutosh Dubey | Data Insights Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">
    <link rel="stylesheet" href="https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css">
    <style>
        body {{ font-family: 'Inter', sans-serif; background-color: #0b0b0b; color: white; scroll-behavior: smooth; }}
        .mono {{ font-family: 'JetBrains Mono', monospace; }}
        .glass-sidebar {{ background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(15px); border-radius: 30px; }}
        .section-tag {{ border: 1px solid #555; padding: 6px 16px; border-radius: 30px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #fff; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 40px; }}
        .neon-text {{ color: #28e98c; }}
        ::-webkit-scrollbar {{ width: 5px; }}
        ::-webkit-scrollbar-track {{ background: #0b0b0b; }}
        ::-webkit-scrollbar-thumb {{ background: #28e98c; border-radius: 10px; }}
        .project-card:hover, .resume-card:hover {{ border-color: #28e98c; transform: translateY(-5px); transition: all 0.3s ease; }}
        .modal {{ display: none; position: fixed; inset: 0; z-index: 100; background: rgba(0,0,0,0.85); backdrop-filter: blur(10px); align-items: center; justify-content: center; padding: 20px; }}
        .modal.active {{ display: flex; }}
    </style>
</head>
<body class="p-4 lg:p-10">
    <aside class="fixed left-6 top-10 bottom-10 w-[320px] hidden lg:flex flex-col p-8 glass-sidebar z-50">
        <div class="flex justify-between items-center mb-10">
            <h2 class="text-2xl font-bold tracking-tighter">ASHU<span class="neon-text">.</span></h2>
            <span class="text-[10px] text-gray-400 uppercase tracking-widest">Data Analyst</span>
        </div>
        <div class="text-center">
            <div class="w-48 h-48 bg-gray-800 rounded-3xl mx-auto mb-6 overflow-hidden border border-white/10">
                <img src="https://i.ibb.co/R4NWJhcc/photo.jpg" alt="Ashutosh Dubey" class="w-full h-full object-cover">
            </div>
            <h1 class="text-xl font-bold mb-2">Ashutosh Dubey</h1>
            <p class="text-gray-500 text-sm mb-8 leading-relaxed">dubeyashutosh099@gmail.com <br> +91 9616902061 <br> Prayagraj, India</p>
        </div>
        <div class="flex justify-center gap-4 mb-10">
            <a href="https://www.linkedin.com/in/ashutosh-dubey-11261140a" target="_blank" class="h-11 w-11 border border-white/10 rounded-full flex items-center justify-center hover:border-[#28e98c] hover:text-[#28e98c] transition duration-300" title="LinkedIn Profile"><i class="lab la-linkedin-in text-xl"></i></a>
            <a href="https://github.com/dubeyashutosh099-blip" target="_blank" class="h-11 w-11 border border-white/10 rounded-full flex items-center justify-center hover:border-[#28e98c] hover:text-[#28e98c] transition duration-300" title="GitHub Profile"><i class="lab la-github text-xl"></i></a>
        </div>
        <a href="{resume_link}" target="_blank" class="mt-auto bg-[#28e98c] text-black py-4 rounded-full font-bold uppercase text-xs tracking-widest hover:scale-105 transition-all flex items-center justify-center gap-2 text-center select-none text-decoration-none">
            <i class="las la-file-download text-base"></i> View / Download Resume
        </a>
    </aside>
    <main class="lg:ml-[380px] pt-10 pb-20">
        <section id="home" class="min-h-screen flex flex-col justify-center" data-aos="fade-up">
            <div class="section-tag"><i class="las la-home"></i> Introduce</div>
            <h2 class="text-5xl lg:text-7xl font-bold leading-tight mb-8">Say Hi from <span class="neon-text italic font-light">Ashu</span>, <br>Turning Data into Stories.</h2>
            <p class="text-gray-400 text-lg max-w-xl mb-12">BCA student with a strong foundation in Data Analysis, SQL, and Python. Passionate about transforming raw data into actionable insights through visualization tools like Power BI and Excel.</p>
            <div class="flex gap-12">
                <div>
                    <h3 class="text-5xl font-bold neon-text">Fresher</h3>
                    <p class="mono text-[10px] text-gray-500 uppercase mt-2 tracking-widest">Data & Ops</p>
                </div>
                <div>
                    <h3 class="text-5xl font-bold neon-text">BCA</h3>
                    <p class="mono text-[10px] text-gray-500 uppercase mt-2 tracking-widest">Education</p>
                </div>
            </div>
        </section>
        <section id="resume" class="py-32" data-aos="fade-up">
            <div class="section-tag"><i class="las la-briefcase"></i> Resume</div>
            <h2 class="text-4xl font-bold mb-12 leading-tight">Experience & <span class="neon-text">Education</span></h2>
            <div class="space-y-12">
                <div class="relative pl-8 border-l border-[#28e98c] group">
                    <div class="absolute w-3 h-3 bg-[#28e98c] rounded-full -left-[6.5px] top-2 shadow-[0_0_10px_#28e98c]"></div>
                    <span class="text-[#28e98c] mono text-xs uppercase tracking-widest font-semibold">July 2026 — Present</span>
                    <h3 class="text-xl font-bold mt-2">Executive</h3>
                    <p class="text-white/80 text-sm mb-4">King Securitas Private Limited</p>
                    <p class="text-gray-400 max-w-2xl text-sm leading-relaxed">Currently deployed at the Gadepan branch, handling operational frameworks and systemic workflow execution for client partner Gtropy Systems Pvt. Ltd. (A MapmyIndia Company) across multiple corporate offices.</p>
                </div>
                <div class="relative pl-8 border-l border-white/10 group">
                    <div class="absolute w-3 h-3 bg-gray-500 rounded-full -left-[6.5px] top-2 group-hover:bg-[#28e98c] transition-colors"></div>
                    <span class="text-gray-500 mono text-xs uppercase tracking-widest">2022 — 2025</span>
                    <h3 class="text-xl font-bold mt-2">Bachelor of Computer Applications (BCA)</h3>
                    <p class="text-[#28e98c] text-sm mb-4">FS University, Shikohabad</p>
                    <p class="text-gray-400 max-w-2xl text-sm leading-relaxed">Pursued technical graduation foundations centered around database structural engineering, object logic systems, and analytical frameworks.</p>
                </div>
                <div class="relative pl-8 border-l border-white/10 group">
                    <div class="absolute w-3 h-3 bg-gray-500 rounded-full -left-[6.5px] top-2 group-hover:bg-[#28e98c] transition-colors"></div>
                    <span class="text-gray-500 mono text-xs uppercase tracking-widest">Jan - Feb 2026</span>
                    <h3 class="text-xl font-bold mt-2">Python & Advanced Excel Analytics</h3>
                    <p class="text-[#28e98c] text-sm mb-4">Technosavvys Education Technology, Allahabad</p>
                    <p class="text-gray-400 max-w-2xl text-sm leading-relaxed">Mastered full-stack calculations, data cleansing pipelines via Pandas/Matplotlib, and comprehensive dashboard reporting utilizing custom Pivot Tables and complex validation arrays.</p>
                </div>
            </div>
            <div class="mt-10 lg:hidden">
                 <a href="{resume_link}" target="_blank" class="w-full max-w-xs bg-[#28e98c] text-black py-4 rounded-full font-bold uppercase text-xs tracking-widest hover:scale-105 transition-all flex items-center justify-center gap-2 text-center text-decoration-none">
                    <i class="las la-file-download text-base"></i> View / Download Resume
                </a>
            </div>
        </section>
        <section id="projects" class="py-32" data-aos="fade-up">
            <div class="section-tag"><i class="las la-grip-vertical"></i> Portfolio</div>
            <h2 class="text-4xl font-bold mb-12 leading-tight">Featured <span class="neon-text">Projects</span></h2>
            <div class="space-y-8">
                <div class="project-card border border-white/10 p-10 rounded-[40px] bg-white/[0.02]">
                    <div class="flex justify-between items-start mb-6">
                        <h3 class="text-2xl font-bold">Employment Dashboard</h3>
                        <span class="text-[#28e98c] mono text-xs uppercase border border-[#28e98c]/30 px-3 py-1 rounded-full">Power BI</span>
                    </div>
                    <p class="text-gray-400 mb-6">Visualizing salary landscapes and data trends using advanced analytics models.</p>
                </div>
            </div>
        </section>
    </main>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({{ duration: 1000, once: false }});
    </script>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=True)