import tkinter as tk
from tkinter import filedialog, scrolledtext
from itertools import zip_longest

def compare_files():
	file1 = entry_file1.get()
	file2 = entry_file2.get()

	if not file1 or not file2:
		text_area.insert(tk.END, "Please select both files.\n")
		return

	try:
		with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
			text_area.delete(1.0, tk.END) # Clear previous output

			diff_found = False
			for line_no, (line1, line2) in enumerate(zip_longest(f1, f2), start=1):
				if line1 != line2:
					diff_found = True
					text_area.insert(tk.END, f"Line {line_no}:\n")
					text_area.insert(tk.END, f" File1: {line1.rstrip('\n') if line1 else '<no line>'}\n")
					text_area.insert(tk.END, f" File2: {line2.rstrip('\n') if line2 else '<no line>'}\n")
					text_area.insert(tk.END, "\n")

			if not diff_found:
				text_area.insert(tk.END, "All lines are identical.\n")
	except FileNotFoundError as e:
		text_area.insert(tk.END, f"Error: {e}\n")
	except UnicodeDecodeError:
		text_area.insert(tk.END, "Error: Files must be UTF-8 encoded.\n")
	except Exception as e:
		text_area.insert(tk.END, f"Unexpected error: {e}\n")

def browse_file(entry):
	filename = filedialog.askopenfilename()
	if filename:
		entry.delete(0, tk.END)
		entry.insert(0, filename)

root = tk.Tk()
root.title("Text File Comparer")
root.geometry("700x500")

frame_top = tk.Frame(root)
frame_top.pack(pady=10, fill=tk.X, padx=10)

tk.Label(frame_top, text="File 1:").grid(row=0, column=0, sticky="w", padx=5)
entry_file1 = tk.Entry(frame_top, width=50)
entry_file1.grid(row=0, column=1, padx=5)
tk.Button(frame_top, text="Browse...", command=lambda: browse_file(entry_file1)).grid(row=0, column=2, padx=5)

tk.Label(frame_top, text="File 2:").grid(row=1, column=0, sticky="w", padx=5)
entry_file2 = tk.Entry(frame_top, width=50)
entry_file2.grid(row=1, column=1, padx=5)
tk.Button(frame_top, text="Browse...", command=lambda: browse_file(entry_file2)).grid(row=1, column=2, padx=5)

btn_compare = tk.Button(root, text="Compare Files", command=compare_files)
btn_compare.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10))
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()