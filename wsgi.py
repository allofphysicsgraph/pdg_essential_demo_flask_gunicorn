#!/usr/bin/env python3

# Physics Derivation Graph
# Ben Payne, 2025
# https://creativecommons.org/licenses/by/4.0/
# Attribution 4.0 International (CC BY 4.0)

"""
this file is for gunicorn

If the app uses Flask, the entry point is at the bottom of pdg_app.py
"""

from pdg_app import web_app

print("hello from wsgi")

if __name__ == "__main__":
    web_app.run()

# EOF
