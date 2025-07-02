import os

def generate_app_routes(paths=None, overwrite=False):
    default_paths = [
        "/about-us",
        "/discover-afrobeats",
        "/artists",
        "/music-releases",
        "/music-releases/latest",
        "/music-videos",
        "/fashion-influence",
        "/events",
        "/blog",
    ]

    paths = paths or default_paths
    base_dir = "src/app"

    print(f"🛠 Generating {len(paths)} routes...")

    for path in paths:
        clean_path = path.lstrip("/")
        full_dir = os.path.join(base_dir, *clean_path.split("/"))
        os.makedirs(full_dir, exist_ok=True)

        page_file = os.path.join(full_dir, "page.tsx")

        if overwrite or not os.path.exists(page_file):
            title = clean_path.split("/")[-1].replace("-", " ").title()
            with open(page_file, "w") as f:
                f.write(f"""export default function Page() {{
    return (
        <div>
            <h1>{title}</h1>
            <p>This is the {clean_path} page.</p>
        </div>
    );
}}
""")

    print("✅  All route folders and page.tsx files created.")
