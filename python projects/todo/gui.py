from __init__ import *

def rebuild_gui(app, frame, entry):
    # clear existing checkboxes
    for widget in frame.winfo_children():
        widget.destroy()
    app.checkbox_vars = []
    for idx, task in enumerate(todo, start=1):
        var = IntVar(value=1 if is_struckthrough(task) else 0)
        cb = ctk.CTkCheckBox(frame,
            text=(f"{idx}. {task}"),
            variable=var,
            onvalue=1, offvalue=0,
            command=lambda i=idx-1, v=var: on_check(i, v, app))
        cb.grid(row=idx, column=0, sticky="w")
        app.checkbox_vars.append(var)

def on_check(index, var, app):
    # index in todo list, var.get() is 1 (checked) or 0
    check(index+1)  # flips strike-through in demo.todo
    rebuild_gui(app, app.cb_frame, app.entry_widget)

def run_app():
    app = ctk.CTk()
    app.title("TO‑DO.ist")
    app.geometry("300x400")

    app.entry_widget = ctk.CTkEntry(app, placeholder_text="Enter your task")
    app.entry_widget.grid(row=0, column=1, padx=10, pady=5)

    add_btn = ctk.CTkButton(app, text="Add task",
                            command=lambda: (
                                add(app.entry_widget.get()),
                                save_tasks(),
                                rebuild_gui(app, app.cb_frame, app.entry_widget)
                            ))
    add_btn.grid(row=1, column=1, padx=10, pady=5)

    delete_btn = ctk.CTkButton(app, text="Delete task",
                               command=lambda: (
                                   delete(app.entry_widget.get()),
                                   save_tasks(),
                                   rebuild_gui(app, app.cb_frame, app.entry_widget)
                               ))
    delete_btn.grid(row=2, column=1, padx=10, pady=5)

    close_btn = ctk.CTkButton(app, text="Close", command=close)
    close_btn.grid(row=3, column=1, padx=10, pady=5)

    app.cb_frame = ctk.CTkFrame(app)
    app.cb_frame.grid(row=0, column=3, columnspan=2, sticky="nsew")

    rebuild_gui(app, app.cb_frame, app.entry_widget)
    app.mainloop()



if __name__ == "__main__":
    run_app()
