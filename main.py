import tkinter as tk
from tkinter import ttk
from sorting_algorithms.algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort
import time

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualization")

        self.algorithms = {
            "Bubble Sort": bubble_sort,
            "Insertion Sort": insertion_sort,
            "Selection Sort": selection_sort,
            "Merge Sort": merge_sort,
        }

        self.sleep_times = {
            "Bubble Sort": 1,
            "Insertion Sort": 1,
            "Selection Sort": 1,
            "Merge Sort": 2,
        }

        self.selected_algorithm = tk.StringVar()
        self.selected_algorithm.set("Bubble Sort")

        self.create_widgets()

    def create_widgets(self):
        # Dropdown for algorithm selection
        algorithm_label = tk.Label(self.root, text="Select Algorithm:")
        algorithm_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        algorithm_dropdown = ttk.Combobox(self.root, textvariable=self.selected_algorithm, values=list(self.algorithms.keys()))
        algorithm_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Text box to input the vector
        vector_label = tk.Label(self.root, text="Enter Vector (comma-separated):")
        vector_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.vector_entry = tk.Entry(self.root)
        self.vector_entry.grid(row=1, column=1, padx=10, pady=5)

        # Button to start sorting
        sort_button = tk.Button(self.root, text="Sort", command=self.sort)
        sort_button.grid(row=2, column=0, columnspan=2, pady=10)

    def sort(self):
        algorithm_name = self.selected_algorithm.get()
        algorithm = self.algorithms[algorithm_name]

        try:
            input_vector = [int(x) for x in self.vector_entry.get().split(",")]
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid vector.")
            return

        sorted_vector = algorithm(input_vector.copy())  # Copy the vector to avoid unwanted modifications

        # Create a window for step-by-step visualization
        step_by_step_window = tk.Toplevel(self.root)
        step_by_step_window.title("Step-by-Step Visualization")
        step_by_step_window.geometry("400x300")

        # Label to display the current step
        step_label = tk.Label(step_by_step_window, text="Step 0")
        step_label.pack(pady=5)

        # Label to display the current vector
        vector_label = tk.Label(step_by_step_window, text=str(input_vector))
        vector_label.pack(pady=10)

        # Label for additional text
        additional_label = tk.Label(step_by_step_window, text="")
        additional_label.pack(pady=5)


        # Function to update the step-by-step visualization
        def update_step(step, vector, current_text=""):
            step_label.config(text=f"Step {step}")
            vector_label.config(text=str(vector))
            additional_label.config(text=current_text)
            step_by_step_window.update()

        # Show the initial vector
        update_step(0, input_vector)

        sleep_time = self.sleep_times.get(algorithm_name, 1)  # Get the corresponding sleep time for the algorithm
        # Execute the algorithm and update the step-by-step visualization
        for i, (step_vector, step_text) in enumerate(zip(sorted_vector[0], sorted_vector[1])):
            time.sleep(sleep_time)
            update_step(i + 1, step_vector, step_text)
        
        time.sleep(1)
        additional_label.config(text="Vector sorted!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
