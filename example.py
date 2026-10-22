import pycristal as pc



def sync_project():
    pc.info("Starting sync for project files...")

    # Simulated work
    pc.success("Downloaded 12 files successfully.")
    pc.warning("3 files were skipped because they were unchanged.")
    pc.info("Applying final checks...")
    pc.success("Project sync completed successfully!")


if __name__ == "__main__":
    sync_project()
    pc.error("This is how an error message looks in PyCristal.")
