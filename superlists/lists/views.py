from django.shortcuts import render
from django.http import httpResponse

# Create your views here.

def home_page():
	return httpResponse('<html><title>To-Do lists</title>')
