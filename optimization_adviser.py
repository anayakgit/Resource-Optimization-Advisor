import psutil
import time

class ResourceOptimizer:
    def __init__(self):
        self.cpu_threshold = 80  #in percentage
        self.memory_threshold = 80 

    def get_system_stats(self):
        """Get system CPU and memory usage statistics."""
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        return cpu_usage, memory_usage

    def check_resource_usage(self, cpu_usage, memory_usage):
        """Check if system resources exceed the threshold."""
        if cpu_usage > self.cpu_threshold:
            print(f"Warning: CPU usage is high at {cpu_usage}%")
            self.suggest_optimizations("CPU")
        if memory_usage > self.memory_threshold:
            print(f"Warning: Memory usage is high at {memory_usage}%")
            self.suggest_optimizations("Memory")

    def suggest_optimizations(self, resource_type):
        """Suggest optimizations based on resource usage."""
        if resource_type == "CPU":
            print("Suggested Optimizations for CPU:")
            print("1. Close unnecessary applications.")
            print("2. Free up system resources by ending heavy processes.")
        elif resource_type == "Memory":
            print("Suggested Optimizations for Memory:")
            print("1. Clear memory cache and temporary files.")
            print("2. Close applications consuming too much memory.")
            print("3. Consider upgrading your RAM for more capacity.")
    
    def monitor_resources(self):
        """Monitor the system's resources in real-time."""
        print("Monitoring system resources...")
        try:
            while True:
                cpu_usage, memory_usage = self.get_system_stats()
                print(f"CPU: {cpu_usage}% | Memory: {memory_usage}%")
                self.check_resource_usage(cpu_usage, memory_usage)
                time.sleep(15)  #check every 15 seconds
        except KeyboardInterrupt:
            print("Resource monitoring stopped.")

def main():
    optimizer = ResourceOptimizer()
    optimizer.monitor_resources()

if __name__ == "__main__":
    main()
