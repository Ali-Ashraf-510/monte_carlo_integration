import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from monte_carlo_integration import monte_carlo_integration

def calculate_integral():
    try:
        func_str = entry_function.get()
        n_points = int(entry_points.get())
        a = float(entry_a.get())
        b = float(entry_b.get())

        def f(x):
            return eval(func_str, {"x": x})

        # إجراء الحساب باستخدام الدالة في الملف المنفصل
        estimated, area_under, area_above, points_under, points_above, max_y, rect_area = monte_carlo_integration(f, a, b, n_points)

        # عرض النتائج في الواجهة
        result_label.config(text=f"Approximate Integral: {estimated:.6f}")
        area_label.config(text=f"Total Rectangle Area: {rect_area:.6f}")
        under_label.config(text=f"Area Under Curve: {area_under:.6f}")
        above_label.config(text=f"Area Above Curve: {area_above:.6f}")
        error_label.config(text=f"Error: {abs(0.5 - estimated):.6f}")

        # رسم الرسم البياني
        plt.figure(figsize=(10, 6))
        plt.title('Monte Carlo Integration by Darts')
        plt.xlabel('x')
        plt.ylabel('y')

        # عرض النقاط تحت وفوق المنحنى
        x_under, y_under = zip(*points_under) if points_under else ([], [])
        x_above, y_above = zip(*points_above) if points_above else ([], [])
        
        plt.scatter(x_under, y_under, color='green', s=10, label='Points Under Curve')
        plt.scatter(x_above, y_above, color='red', s=10, label='Points Above Curve')

        x_curve = [x / 1000 for x in range(int(a * 1000), int(b * 1000))]
        y_curve = [f(x) for x in x_curve]
        plt.plot(x_curve, y_curve, color='blue', linewidth=2, label=f'f(x) = {func_str}')
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# تصميم الواجهة
app = tk.Tk()
app.title("Monte Carlo Integration GUI")
app.geometry("500x500")
app.configure(bg="#2e2e2e")

header = tk.Label(app, text="Monte Carlo Integration Calculator", font=("Arial", 16, "bold"), bg="#2e2e2e", fg="#00ff00")
header.pack(pady=10)

frame = tk.Frame(app, bg="#2e2e2e")
frame.pack(pady=10)

tk.Label(frame, text="Function (in terms of x):", bg="#2e2e2e", fg="white").grid(row=0, column=0, sticky="w")
entry_function = tk.Entry(frame, width=30)
entry_function.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Number of Points:", bg="#2e2e2e", fg="white").grid(row=1, column=0, sticky="w")
entry_points = tk.Entry(frame, width=30)
entry_points.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Range Start (a):", bg="#2e2e2e", fg="white").grid(row=2, column=0, sticky="w")
entry_a = tk.Entry(frame, width=30)
entry_a.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Range End (b):", bg="#2e2e2e", fg="white").grid(row=3, column=0, sticky="w")
entry_b = tk.Entry(frame, width=30)
entry_b.grid(row=3, column=1, pady=5)

calculate_button = tk.Button(app, text="Calculate", command=calculate_integral, bg="#007acc", fg="white")
calculate_button.pack(pady=10)

result_label = tk.Label(app, text="", bg="#2e2e2e", fg="#00ff00", font=("Arial", 12))
result_label.pack()

area_label = tk.Label(app, text="", bg="#2e2e2e", fg="#00ff00", font=("Arial", 12))
area_label.pack()

under_label = tk.Label(app, text="", bg="#2e2e2e", fg="#00ff00", font=("Arial", 12))
under_label.pack()

above_label = tk.Label(app, text="", bg="#2e2e2e", fg="#00ff00", font=("Arial", 12))
above_label.pack()

error_label = tk.Label(app, text="", bg="#2e2e2e", fg="#00ff00", font=("Arial", 12))
error_label.pack()

app.mainloop()
