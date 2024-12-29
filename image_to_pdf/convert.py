import tkinter as tk
from tkinter import filedialog

class ImageToPDFConvert:
    def __init__(self, root):
        self.root = root
        self.image_path = []
        self.output_pdf_name = tk.StringVar()
        self.selected_image_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        
        self.initiaalize_ui()
    
    def initiaalize_ui(self):
        title_label = tk.Label(self.root, text='IMG TO PDF', font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=10)
        
        select_image_button = tk.Button(self.root, text='Select Image', command=self.select_images)
        select_image_button.pack(padx=(0, 10))
        
def main():
    root = tk.Tk()
    root.title('Image to PDF')
    convert = ImageToPDFConvert(root)
    root.geometry('400x600')
    root.mainloop()

if __name__ == '__main__':
    main()