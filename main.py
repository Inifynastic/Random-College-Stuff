import tkinter as tk
from tkinter import ttk, messagebox

# The entire tkinter code was converted from QTcreator(xml file) to tkinter hence OOP followed
class PromptManagerUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prompt Manager")
        self.geometry("800x600")
        self.minsize(800, 600)

         # Global Variables(Kind of)
        self._FILE_NAME = "prompts.txt"
        self._PROMPTS_LIST = []

        self._build_form_section()
        self._build_button_section()
        self._build_separator()
        self._build_text_sections()
        self._sync_storage_memory()

    def _build_form_section(self):
        form_frame = ttk.Frame(self)
        form_frame.place(x=30, y=20, width=310, height=115)

        # Prompt Title
        ttk.Label(form_frame, text="Prompt Title:").grid(
            row=0, column=0, sticky="w", padx=5, pady=6
        )
        self.entry_title = ttk.Entry(form_frame, width=28)
        self.entry_title.grid(row=0, column=1, sticky="ew", padx=5, pady=6)

        # AI Tool
        ttk.Label(form_frame, text="AI Tool:").grid(
            row=1, column=0, sticky="w", padx=5, pady=6
        )
        self.entry_tool = ttk.Combobox(
            form_frame,
            values=["ChatGPT", "Claude", "Gemini", "Copilot", "Midjourney"],
            state="readonly",
            width=26,
        )
        self.entry_tool.grid(row=1, column=1, sticky="ew", padx=5, pady=6)

        # Category
        ttk.Label(form_frame, text="Category:").grid(
            row=2, column=0, sticky="w", padx=5, pady=6
        )
        self.entry_category = ttk.Combobox(
            form_frame,
            values=["Programming", "Writing", "Art", "Analysis", "Other"],
            state="readonly",
            width=26,
        )
        self.entry_category.grid(row=2, column=1, sticky="ew", padx=5, pady=6)

        # Rating [1-5]
        ttk.Label(form_frame, text="Rating[1-5]:").grid(
            row=3, column=0, sticky="w", padx=5, pady=6
        )
        self.entry_rating = ttk.Combobox(
            form_frame, values=["1", "2", "3", "4", "5"], state="readonly", width=26
        )
        self.entry_rating.grid(row=3, column=1, sticky="ew", padx=5, pady=6)

        form_frame.columnconfigure(1, weight=1)

    def _build_button_section(self):
        btn_frame = ttk.Frame(self)
        btn_frame.place(x=370, y=20, width=400, height=111)

        buttons = [
            ("Add Prompt", self._add_prompt_handler, 0, 0),
            ("Display All", self._display_all_handler, 0, 1),
            ("Search", self._search_prompt_handler, 0, 2),
            ("Delete", self._delete_prompt_handler, 1, 0),
            ("Update", self._update_prompt_handler, 1, 1),
            ("Clear Field", self._clear_entries, 1, 2),
        ]
        
        for text, cmd, r, c in buttons:
            b = ttk.Button(btn_frame, text=text, command=cmd)
            b.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)

        for c in range(3):
            btn_frame.columnconfigure(c, weight=1)
        for r in range(2):
            btn_frame.rowconfigure(r, weight=1)

    # ------------------------------------------------------------------
    # Horizontal separator line
    # ------------------------------------------------------------------
    def _build_separator(self):
        sep = ttk.Separator(self, orient="horizontal")
        sep.place(x=30, y=150, width=740)

    # ------------------------------------------------------------------
    # Bottom section: Prompt Text (left) / Result-All Prompts (right)
    # ------------------------------------------------------------------
    def _build_text_sections(self):
        # Left label + text box
        ttk.Label(self, text="Prompt Text").place(x=20, y=170)
        self.entry_prompt_text = tk.Text(self, wrap="word")
        self.entry_prompt_text.place(x=20, y=200, width=291, height=341)

        # Right label + text box (used as read-only output/result area)
        ttk.Label(self, text="Result / All Prompts:").place(x=360, y=178)
        self.result_text = tk.Text(self, wrap="word")
        self.result_text.place(x=360, y=200, width=401, height=341)

    
    # ------------------------------------------------------------------
    # TKINTER HANDLER FUNCTIONS (I had to add this with slight modification since my generated code did not come with one)
    # ------------------------------------------------------------------
    def _add_prompt_handler(self):
        title = self.entry_title.get()
        prompt_text = self.entry_prompt_text.get('1.0', tk.END).strip().replace('\n', ' ')
        tool = self.entry_tool.get()
        category = self.entry_category.get()
        rating = self.entry_rating.get()

        result = self._add_prompt(title, prompt_text, tool, category, rating)
        messagebox.showinfo("Result", result)
        if result.startswith("Successfully Added"):
            self._clear_entries()
            self._display_all_prompt(self.result_text)
    
    def _display_all_handler(self):
        self._display_all_prompt(self.result_text)

    def _search_prompt_handler(self):
        title = self.entry_title.get()
        if title:
            results = self._search_prompt(title)
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, f"Search results for '{title}':\n\n")
            if results:
                for r in results:
                    self.result_text.insert(tk.END, r + "\n" + "-"*40 + "\n")
            else:
                self.result_text.insert(tk.END, "Prompt not found.")
        else:
            messagebox.showwarning("Input Error", "Enter a title to search.")

    def _delete_prompt_handler(self):
        title = self.entry_title.get()
        if title:
            result = self._delete_prompt(title)
            messagebox.showinfo("Result", result)
            if result.startswith("SUCCESS"):
                self._clear_entries()
                self._display_all_prompt(self.result_text)
        else:
            messagebox.showwarning("Input Error", "Enter the title to delete.")

    def _update_prompt_handler(self):
        old_title = self.entry_title.get()
        new_title = self.entry_title.get() 
        new_prompt_text = self.entry_prompt_text.get('1.0', tk.END).strip().replace('\n', ' ')
        new_tool = self.entry_tool.get()
        new_category = self.entry_category.get()
        new_rating = self.entry_rating.get()
        
        if old_title:
            result = self._update_prompt(old_title, new_title, new_prompt_text, new_tool, new_category, new_rating)
            messagebox.showinfo("Result", result)
            if result.startswith("SUCCESS"):
                self._clear_entries()
                self._display_all_prompt(self.result_text)
        else:
            messagebox.showwarning("Input Error", "Enter the title to update.")
    # ------------------------------------------------------------------
    # Main Functions
    # ------------------------------------------------------------------
    def _add_prompt(self, title, prompt_text, tool, category, rating):
        self._PROMPTS_LIST# Techinally a global variable since all the member of the class can access it
        if title and tool and prompt_text: 
        #---Add your code between these comments
            self._PROMPTS_LIST.append([title , prompt_text,tool, category, rating]) #  I used w3school for syntax
            self._sync_memory_storage()
        #---------------------------------------
            return f"Successfully Added: {title}"
        else:
            return "Error: Title, Prompt Text, and AI Tool are required."

    def _display_all_prompt(self, display_output_widget):
        display_output_widget.delete('1.0', tk.END) 
        display_output_widget.insert(tk.END, "--- ALL PROMPTS ---\n")
        #---Add your code between these comments
        for i in range(len(self._PROMPTS_LIST)):
            display_output_widget.insert(tk.END, f"Title: {self._PROMPTS_LIST[i][0]}, Prompt Text: {self._PROMPTS_LIST[i][1]}, Tool: {self._PROMPTS_LIST[i][2]}, Catgory: {self._PROMPTS_LIST[i][3]}, Rating: {self._PROMPTS_LIST[i][4]}\n")

        display_output_widget.insert(tk.END, f"Total Prompt: {len(self._PROMPTS_LIST)}")
        #---------------------------------------

    def _search_prompt(self, search_title):
        found_prompts = []
        if not search_title:
            return []

        search_term = search_title.lower()
    
        #---Add your code between these comments
        for i in range(len(self._PROMPTS_LIST)):
            if (self._PROMPTS_LIST[i][0].lower() == search_term):
                found_prompts.append(self._PROMPTS_LIST[i][0])
        return found_prompts
        #---------------------------------------

    def _delete_prompt(self, target_title):
        self._PROMPTS_LIST
        if not target_title:
            return "Error: Target title cannot be empty."

        target_lower = target_title.lower()
    
        #---Add your code between these comments
        for i in range(len(self._PROMPTS_LIST)):
            if (self._PROMPTS_LIST[i][0].lower() == target_lower):
                self._PROMPTS_LIST.pop(i)
                self._sync_memory_storage()
                return "Success: Target title deleted."
        #---------------------------------------

        return f"FAILURE: Prompt '{target_title}' not found."

    def _update_prompt(self, old_title, new_title, new_prompt_text, new_tool, new_category, new_rating):
        self._PROMPTS_LIST
        if not old_title:
            return "Error: Old title cannot be empty."

        old_title_lower = old_title.lower()
    
        #---Add your code between these comments
        for i in range(len(self._PROMPTS_LIST)):
            if (self._PROMPTS_LIST[i][0].lower() == old_title_lower):

                self._PROMPTS_LIST[i][0] = new_title
                self._PROMPTS_LIST[i][1] = new_prompt_text
                self._PROMPTS_LIST[i][2] = new_tool
                self._PROMPTS_LIST[i][3] = new_category
                self._PROMPTS_LIST[i][4] = new_rating
                self._sync_memory_storage()
                return f"SUCCESS: Prompt '{old_title}' updated."
        #---------------------------------------
    
        return f"FAILURE: Prompt '{old_title}' not found for update."

    def _clear_entries(self):
        self.entry_title.delete(0, tk.END)
        self.entry_tool.set("")
        self.entry_category.set("")
        self.entry_rating.set("")
        self.entry_prompt_text.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
    # ------------------------------------------------------------------
    # Extra Functions
    # ------------------------------------------------------------------
    def _sync_storage_memory(self):
            with open(self._FILE_NAME, "r") as f:
                for line in f:
                    i = 0
                    current = ""
                    field = []
                    while(i< len(line)):
                        if(line[i:i+3] == "|~|"):
                            field.append(current)
                            current = ""
                            i += 3
                        else:
                            current += line[i]
                            i += 1
                    field.append(current)
                    self._PROMPTS_LIST.append(field)
                
    def _sync_memory_storage(self):
        with open(self._FILE_NAME, "w") as f:
            for data in self._PROMPTS_LIST:
                for j in range(0,5):
                    f.write(data[j])
                    if j != 4:
                        f.write("|~|") 
                f.write("\n") 
                
                 


if __name__ == "__main__":
    app = PromptManagerUI()
    app.mainloop()


