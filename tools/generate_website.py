import os

repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_report_path = os.path.join(repo_dir, "report", "Lab_Evaluation_Report.html")
index_html_path = os.path.join(repo_dir, "index.html")

with open(html_report_path, "r", encoding="utf-8") as f:
    html = f.read()

navbar_css = """
    .top-nav {
        position: sticky;
        top: 0;
        z-index: 1000;
        background: rgba(24, 43, 73, 0.96);
        backdrop-filter: blur(8px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 28px;
        margin: -20px -20px 25px -20px;
        border-bottom: 2px solid #107c82;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.18);
    }
    .top-nav .brand {
        font-weight: 700;
        color: #ffffff;
        font-size: 17px;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .top-nav .links {
        display: flex;
        gap: 12px;
    }
    .top-nav a.btn {
        background: #107c82;
        color: white;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .top-nav a.btn:hover {
        background: #159b9f;
        transform: translateY(-1px);
    }
    .top-nav a.btn-outline {
        background: transparent;
        border: 1px solid #107c82;
        color: #e0f2f1;
    }
    .top-nav a.btn-outline:hover {
        background: rgba(16, 124, 130, 0.25);
    }
    .content-wrapper {
        max-width: 1100px;
        margin: 0 auto;
    }
"""

navbar_html = """
<div class="top-nav">
    <a href="https://github.com/Adarshb-2255/openmp-vs-mpi-data-processing" class="brand" target="_blank">
        ⚡ OpenMP vs MPI Benchmark | Adarsh Benawadi
    </a>
    <div class="links">
        <a href="https://github.com/Adarshb-2255/openmp-vs-mpi-data-processing" class="btn btn-outline" target="_blank">GitHub Repository</a>
        <a href="report/Lab_Evaluation_Report.pdf" class="btn" target="_blank">Download PDF Report</a>
        <a href="presentation/OpenMP_vs_MPI_Data_Processing.pptx" class="btn btn-outline" target="_blank">Download Slides (.pptx)</a>
    </div>
</div>
<div class="content-wrapper">
"""

html = html.replace("</style>", navbar_css + "\n</style>", 1)
html = html.replace("<body>", "<body>\n" + navbar_html, 1)
html = html.replace("</body>", "</div>\n</body>", 1)

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated standalone website: {index_html_path} ({os.path.getsize(index_html_path)/1024:.1f} KB)")
