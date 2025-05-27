import time

tasks = {
    "Must have": ["Login system", "User dashboard", "Database setup"],
    "Should have": ["Notifications", "User profile customization"],
    "Could have": ["Dark mode", "Language selection"],
    "Won't have": ["3D animations", "AR support"]
}

def delay(msg):
    print(msg)
    time.sleep(1)

def pre_project():
    delay("\n[Phase 1: Pre-Project]")
    delay("Defining business value and goals...")
    delay("Goal: Create a functional user platform for a school project.\n")

def foundations():
    delay("[Phase 2: Foundations]")
    delay("Analyzing feasibility and outlining requirements...")
    for priority, items in tasks.items():
        print(f"\n{priority} tasks:")
        for item in items:
            print(f"- {item}")
    print()

def evolutionary_development():
    delay("[Phase 3: Evolutionary Development]")
    for priority in ["Must have", "Should have", "Could have"]:
        delay(f"Working on {priority} tasks:")
        for task in tasks[priority]:
            print(f"  Developing: {task}")
            time.sleep(0.5)
        print()
    print("Skipping 'Won't have' tasks.\n")

def deployment():
    delay("[Phase 4: Deployment]")
    delay("Running final tests...")
    delay("Deploying the solution...")
    delay("Project successfully completed!\n")

def main():
    pre_project()
    foundations()
    evolutionary_development()
    deployment()

if __name__ == "__main__":
    main()
