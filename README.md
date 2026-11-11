# Parking SV — Python Desktop Prototype

[English](README.md) | [Español](README.es.md)

## Overview

This repository contains a separate Python desktop prototype associated with Parking SV. It explores how a parking-discovery experience could be presented inside a desktop application using **BeeWare Toga** and an embedded web view.

It is a distinct codebase from the Parking SV Next.js web application. The two repositories have separate implementations and source histories.

## What the prototype contains

- Welcome, navigation and home screens.
- Sign-in and registration forms shown as interface examples.
- A parking catalogue with text search over predefined sample records.
- Parking detail views with sample schedules, rates, descriptions, images, services and restrictions.
- Profile, notification, contact and subscription-plan screens.
- External navigation links, including Waze links attached to sample parking records.

The interface is primarily in Spanish and uses a responsive layout designed for the application's embedded web view.

## How it works

The Python layer is a lightweight desktop shell:

1. **Parking_SV/__main__.py** starts the application.
2. **Parking_SV/app.py** creates a Toga MainWindow.
3. The app reads **resources/Index.html** from its packaged resources.
4. A Toga WebView displays the HTML interface inside the native application window.
5. JavaScript embedded in the HTML switches between screens, filters the local parking sample list and renders parking details.

The visual interface is implemented in a single HTML resource with embedded CSS and JavaScript. **pyproject.toml** contains the Briefcase packaging metadata and platform-specific Toga dependencies.

## Prototype boundaries

This repository should be evaluated as a UI and desktop-integration prototype, not as a live parking service.

- Parking records are predefined in the frontend; they are not retrieved from a production API.
- Search filters the local sample list.
- Sign-in and registration screens do not authenticate users or create accounts.
- Reservation, availability and notification examples are not connected to a live service.
- The contact form does not send messages.
- No payment processing, real-time inventory, server-side application or database integration is implemented in this codebase.

Names, prices, contact details, images and parking descriptions in the interface are sample content and must not be treated as verified business information.

## Technology

- Python 3
- BeeWare Toga
- Briefcase
- Toga WebView
- HTML5, CSS3 and JavaScript

## Run in development mode

The Briefcase project is located in the **Parking-SV/** directory.

~~~bash
cd Parking-SV
python -m venv .venv
~~~

Activate the environment:

**Windows PowerShell**
~~~powershell
.venv\Scripts\Activate.ps1
~~~

**Linux / macOS**
~~~bash
source .venv/bin/activate
~~~

Install Briefcase and run the application in development mode:

~~~bash
python -m pip install briefcase
briefcase dev
~~~

Native dependencies vary by operating system. The platform-specific configuration is declared in **pyproject.toml**.

## Source layout

~~~text
Parking-SV/
├── pyproject.toml
├── src/Parking_SV/
│   ├── __main__.py
│   ├── app.py
│   └── resources/
│       └── Index.html
└── tests/
~~~

## Related project

- [Parking SV — Next.js web application](https://github.com/parkingSV26/parkingsv-web)
- [Public Parking SV web experience](https://parkingsv.vercel.app/)

The Python prototype is a separate implementation reference. Its functionality and contributors should not be conflated with those of the Next.js project.
