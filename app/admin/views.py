# coding: utf8
from . import admin
from flask import render_template, redirect, url_for

@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/logic')
def login():
    return render_template('admin/login.html')

@admin.route('/logout')
def logout():
    return redirect(url_for('back.index'))
