import tkinter as tk
import threading
import foe
import keyboard
from PIL import Image, ImageTk
import os
import time
import cv2
import numpy as np
import sys
import pygetwindow as gw
import pyautogui
import mouse


class App:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.thread = None
        self.image = Image.open(images/foelogo.jpg')
        self.image = ImageTk.PhotoImage(self.image)



        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.pack()

        self.start_button = tk.Button(self.root, text='Start', command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text='Stop', command=self.stop, state='disabled')
        self.stop_button.pack()

        if self.Web_browser_condition():
            self.display_found_message()
        else:
            self.display_not_found_message()

        self.money_label = tk.Label(self.root, text="")
        self.money_label.pack()

        self.hammer_label = tk.Label(self.root, text="")
        self.hammer_label.pack()

        self.pack_label = tk.Label(self.root, text="")
        self.pack_label.pack()

        self.pack_produce_label = tk.Label(self.root, text="")
        self.pack_produce_label.pack()

        self.production_label = tk.Label(self.root, text="")
        self.production_label.pack()

        self.redeem_label = tk.Label(self.root, text="")
        self.redeem_label.pack()

        self.soldier_label = tk.Label(self.root, text="")
        self.soldier_label.pack()

        self.star_label = tk.Label(self.root, text="")
        self.star_label.pack()

        self.support_label = tk.Label(self.root, text="")
        self.support_label.pack()

        self.train_label = tk.Label(self.root, text="")
        self.train_label.pack()

        self.X_button_label = tk.Label(self.root, text="")
        self.X_button_label.pack()

        money_exists, hammer_exists, pack_exists, pack_produce_exists, production_exists, redeem_exists, soldier_exists, star_exists, support_exists, train_exists, X_button_exists = self.check_images()

        if money_exists:
            self.money_label.config(text="money.jpg exists in the images folder.")
        else:
            self.money_label.config(text="money.jpg does not exist in the images folder.",fg="red")

        if hammer_exists:
            self.hammer_label.config(text="hammer.jpg exists in the images folder.")
        else:
            self.hammer_label.config(text="hammer.jpg does not exist in the images folder.",fg="red")

        if pack_exists:
            self.pack_label.config(text="pack.jpg exists in the images folder.")
        else:
            self.pack_label.config(text="pack.jpg does not exist in the images folder.",fg="red")

        if pack_produce_exists:
            self.pack_produce_label.config(text="pack_produce.jpg exists in the images folder.")
        else:
            self.pack_produce_label.config(text="pack_produce.jpg does not exist in the images folder.",fg="red")

        if production_exists:
            self.production_label.config(text="production.jpg exists in the images folder.")
        else:
            self.production_label.config(text="production.jpg does not exist in the images folder.",fg="red")

        if redeem_exists:
            self.redeem_label.config(text="production.jpg exists in the images folder.")
        else:
            self.redeem_label.config(text="production.jpg does not exist in the images folder.",fg="red")

        if soldier_exists:
            self.soldier_label.config(text="production.jpg exists in the images folder.")
        else:
            self.soldier_label.config(text="production.jpg does not exist in the images folder.",fg="red")

        if star_exists:
            self.star_label.config(text="production.jpg exists in the images folder.")
        else:
            self.star_label.config(text="production.jpg does not exist in the images folder.",fg="red")

        if support_exists:
            self.support_label.config(text="production.jpg exists in the images folder.")
        else:
            self.support_label.config(text="production.jpg does not exist in the images folder.",fg="red")

        if train_exists:
            self.train_label.config(text="production.jpg exists in the images folder.")
        else:
            self.train_label.config(text="production.jpg does not exist in the images folder.",fg="red")

        if X_button_exists:
            self.X_button_label.config(text="production.jpg exists in the images folder.")
        else:
            self.X_button_label.config(text="production.jpg does not exist in the images folder.",fg="red")

        """
            Change to set another hotkey

            :return:
            """
        keyboard.add_hotkey('ctrl + a', self.start)
        keyboard.add_hotkey('ctrl + space', self.stop)

    def start(self, event=None):
        if self.Web_browser_condition():
            self.running = True
            self.thread = threading.Thread(target=self.run_foe)
            self.thread.start()
            self.start_button.config(state='disabled')
            self.stop_button.config(state='normal')

    def stop(self, event=None):
        self.running = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

    def display_not_found_message(self):
        # Display message on GUI
        not_found_label = tk.Label(self.root, text="Forge of Empires - Google Chrome not found",fg="red")
        not_found_label.pack()
    def display_found_message(self):
        not_found_label = tk.Label(self.root, text="Forge of Empires - Google Chrome found", fg="black")
        not_found_label.pack()

    def Web_browser_condition(self):
        Web_browser = gw.getWindowsWithTitle('Forge of Empires - Google Chrome')
        return Web_browser
    def check_images(self):
        images_folder = "images"
        money_image_exists = os.path.exists(os.path.join(images_folder, "money.jpg"))
        hammer_image_exists = os.path.exists(os.path.join(images_folder, "hammer.jpg"))
        pack_exists = os.path.exists(os.path.join(images_folder, "pack.jpg"))
        pack_produce_exists = os.path.exists(os.path.join(images_folder, "pack_produce.jpg"))
        production_exists = os.path.exists(os.path.join(images_folder, "production.jpg"))
        redeem_exists = os.path.exists(os.path.join(images_folder, "redeem.jpg"))
        soldier_exists = os.path.exists(os.path.join(images_folder, "soldier.jpg"))
        star_exists = os.path.exists(os.path.join(images_folder, "star.jpg"))
        support_exists = os.path.exists(os.path.join(images_folder, "support.jpg"))
        train_exists = os.path.exists(os.path.join(images_folder, "train.jpg"))
        X_button_exists = os.path.exists(os.path.join(images_folder, "X_button.jpg"))
        return (money_image_exists, hammer_image_exists, pack_exists, pack_produce_exists, production_exists,
                redeem_exists, soldier_exists, star_exists, support_exists, train_exists, X_button_exists)

    def run_foe(self):
        if self.Web_browser_condition():
            while self.running:
                foe.get_Picture_FOE()
        else:
            print("Window not found")

root = tk.Tk()
app = App(root)
root.mainloop()
keyboard.wait()
