# # production-ready thread pool implementation
# import concurrent.futures
#
#
# def my_task(arg):
#     # Your task code here
#     print(f"Task executed with arg: {arg}")
#
#
# # Create a thread pool with 3 worker threads
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     # Submit tasks to the pool
#     for i in range(5):
#         executor.submit(my_task, i)


import threading
import queue


class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.task_queue = queue.Queue()
        self.workers = []
        self._create_workers()

    def _create_workers(self):
        for _ in range(self.num_threads):
            worker = threading.Thread(target=self._worker_loop)
            self.workers.append(worker)
            worker.start()

    def _worker_loop(self):
        while True:
            task = self.task_queue.get()
            if task is None:
                # None is used as a signal to stop the worker
                break
            # Execute the task
            task()
            # task_done() method is called by the worker thread to indicate that it has completed processing a task
            self.task_queue.task_done()

    def submit(self, task):
        # Add a task to the task queue
        self.task_queue.put(task)

    def join(self):
        # Wait for all tasks to be processed
        self.task_queue.join()

    def shutdown(self):
        # Stop all worker threads
        for _ in range(self.num_threads):
            self.task_queue.put(None)
        for worker in self.workers:
            worker.join()


# Example usage of the ThreadPool
def my_task(task_num):
    print(f"Executing Task {task_num}")


if __name__ == "__main__":
    threads_num = 3
    thread_pool = ThreadPool(threads_num)

    for i in range(10):
        thread_pool.submit(lambda num=i: my_task(num))

    thread_pool.join()
    thread_pool.shutdown()
