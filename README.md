<p align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2xscjB6YXFmemF1bHlqbW11ZWlzemo4bm5zMWU5aWt2ejY0Y3RuNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Tl25hw4bD37AQ/giphy.gif" width="50%" alt="Reinforced Concrete Design Banner">
</p>

# Reinforced Concrete Design II

### Educational Repository for Concrete Design and Structural Engineering

**Authors:** Msc. Ing. Carlos Andrés Celi Sánchez · Nicolás Mora Bowen · Juan Sebastián Baquero  
**Semester:** FEB – 2026

This repository supports the teaching process of the **Reinforced Concrete Design II** course during the current academic semester. It progressively includes theoretical notes, design criteria, Python-based educational tools, numerical examples, and class materials for the strength design of reinforced-concrete members — from material behavior to safe, ductile, durable, and constructible structures.

This repository is **currently under construction** and will continue to be updated throughout the semester as new topics are covered in class.

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
</p>

## Course Roadmap

This repository is expected to progressively cover topics such as:

- Design basis: assumptions, loads, units, and governing limit states
- Flexure and sections: strain compatibility and nominal resistance
- Columns: axial load, moment, slenderness, confinement, and interaction diagrams
- Slabs: one-way and two-way systems, gravity load distribution, and serviceability
- Shear and detailing: preventing brittle behavior and ensuring constructible reinforcement
- Special components: stairs, walls, and foundations connected to the structural system
- Seismic concepts: capacity design and ductile detailing

## Current Contents

At its current stage, the repository includes:

- `Markdowns/00_Introduction.ipynb` — theory: design philosophy, limit states, strength vs. capacity design, ACI 318-25 framework
- `Markdowns/01_Loads.ipynb` — theory: gravity and lateral actions, load symbols, factored combinations, dead/live load takeoff
- `Markdowns/02_Flexure_Behavior.ipynb` — theory: flexural equilibrium, strain compatibility, cracking, yielding, ductility, moment-curvature
- `Markdowns/03_Flexural_Strength_Design.ipynb` — theory: equivalent Whitney block, strength reduction factor, reinforcement limits, flanged and general beam sections
- `Markdowns/04_Slab_Behavior.ipynb` — theory: slab history and typology, one-way and two-way action, two-way (punching) shear, correlation with ACI CODE-318-25 Chapters 7 and 8
- `Markdowns/05_Slab_Design.ipynb` — theory: Direct Design Method scope and limitations, total factored static moment, longitudinal distribution, column and middle strips, minimum reinforcement
- `Markdowns/06_Two_Way_Shear_Design.ipynb` — theory: punching shear mechanism, critical section, two-way shear strength provided by concrete, size effect factor, eccentric shear transfer
- `Markdowns/ACI_318-25_Reading_Plan.ipynb` — a 15-week self-study reading plan through the ACI CODE-318-25 chapters and sections governing slabs, columns, and beam-column connections
- `Examples/Basic_Coding.ipynb` — initial coding example for the course package
- `Examples/Slab.ipynb` — applied example: one-way and two-way action classification from slab and panel data
- The reusable Python package and setup files for future computational implementations

## Repository Structure

    Repo_ConcreteII_Desing/
    │── Markdowns/
    │   ├── 00_Introduction.ipynb
    │   ├── 01_Loads.ipynb
    │   ├── 02_Flexure_Behavior.ipynb
    │   ├── 03_Flexural_Strength_Design.ipynb
    │   ├── 04_Slab_Behavior.ipynb
    │   ├── 05_Slab_Design.ipynb
    │   ├── 06_Two_Way_Shear_Design.ipynb
    │   ├── ACI_318-25_Reading_Plan.ipynb
    │   └── assets/
    │── Examples/
    │   ├── Basic_Coding.ipynb
    │   └── Slab.ipynb
    │── repo__CORE_concreteII_desing/
    │   ├── __init__.py
    │   └── core.py
    │── README.md
    │── requirements.txt
    │── setup.py

> **Note:** The repository structure may evolve during the semester as new material is incorporated.

## Normative Framework

This course uses **ACI CODE-318-25 — Building Code Requirements for Structural Concrete and Commentary** as its principal design reference. In Ecuador, the applicable provisions of the **Norma Ecuatoriana de la Construcción (NEC)** and the requirements of the authority having jurisdiction must be checked for each project. Standards such as ASCE 7 and ASCE 41 are valuable companions when the problem involves load definition, existing structures, or seismic evaluation.

## Prerequisites

Before working with this repository, students should make sure that the following software is installed on their computers:

- **Python 3.10 or newer**
- **Git**
- **Visual Studio Code**
- **Python extension for VS Code**
- **Jupyter extension for VS Code**

These tools are necessary to clone the repository, create the Python environment, open the project correctly in Visual Studio Code, and run both Python scripts and notebooks.

## Installation Guide for Windows and VS Code

This section explains how to correctly install and run the repository on **Windows** using **Visual Studio Code**.

### Step 1. Open the Windows terminal

Before doing anything else, students should first open a standard **Windows terminal**.

They may use any of the following:

- **Command Prompt**
- **Windows PowerShell**

For this course, the recommended option is:

> **Command Prompt**

This helps avoid confusion with terminal commands, file paths, and virtual environment activation steps.

### Step 2. Clone the repository

Once the Windows terminal is open, run:

```bash
    git clone https://github.com/Normando1945/Repo_ConcreteII_Desing.git
```

This command will download the repository to the current folder.

### Step 3. Move into the repository folder

After cloning the repository, enter the project folder with:
```bash
    cd Repo_ConcreteII_Desing
```
From this point on, all commands should be executed inside this folder.

### Step 4. Open the repository in Visual Studio Code

Now that the repository already exists on the computer, open it in **Visual Studio Code** by running:
```bash
    code .
```
If this command does not work, students can simply open **Visual Studio Code** manually and then select the cloned repository folder.

### Step 5. Open the integrated terminal in VS Code

Once the repository has been opened in VS Code, it is recommended that students continue working from the **integrated terminal** inside VS Code.

To open the terminal in VS Code:

- Press **Ctrl + Shift + `**
- Or go to the top menu and select:  
  **Terminal > New Terminal**

A terminal panel will appear at the bottom of Visual Studio Code.

### Step 6. Verify that the terminal is Command Prompt

Inside VS Code, verify that the selected terminal is:

- **Command Prompt**

If another terminal appears and students want to change it:

1. Click the dropdown menu in the terminal panel
2. Select **Command Prompt**
3. Open a new terminal

From this point on, it is recommended that all commands be executed from this terminal in VS Code.

### Step 7. Create a virtual environment

It is strongly recommended to create a virtual environment so that all students work with the same isolated Python setup.

Run:
```bash
    python -m venv venv
```
This command will create a folder called `venv` inside the repository.

### Step 8. Activate the virtual environment in Windows

If students are using **Command Prompt**, run:
```bash
    venv\Scripts\activate
```
After activation, `(venv)` should appear at the beginning of the terminal line. This indicates that the virtual environment is active.

### Step 9. Install the required dependencies

Once the virtual environment has been activated, install the required Python libraries with:
```bash
    pip install -r requirements.txt
```
This step installs all the packages needed by the repository.

### Step 10. Install the repository in editable mode

To allow Python to recognize the package correctly while developing and testing the code, run:
```bash
    pip install -e .
```
This is useful because the package can be modified during the semester without reinstalling it every time.

### Step 11. Install Jupyter support inside the environment

If students are going to work with notebooks in VS Code, it is recommended to also install `ipykernel`:
```bash
    pip install ipykernel
```
Then register the environment as a Jupyter kernel:
```bash
    python -m ipykernel install --user --name=venv --display-name "Python (Concrete Design II)"
```
This will allow students to select the correct Python environment when opening notebooks.

### Step 12. Select the correct interpreter in VS Code

Inside **Visual Studio Code**, follow these steps:

1. Press **Ctrl + Shift + P**
2. Search for: `Python: Select Interpreter`
3. Choose the interpreter corresponding to the `venv` environment

If a notebook is opened, also make sure that the selected kernel is:

`Python (Concrete Design II)`

### Step 13. Verify that the installation works correctly

A simple way to verify the installation is to open Python and try importing the main package.

Run:
```bash
    python
```
Then type:
```bash
    from repo__CORE_concreteII_desing import SimpleMatrixStack
    print("Package imported successfully")
```
If no error appears, the installation was completed correctly.

## First Stage of the Repository

Since the repository is still being developed, the first stage is focused on building a solid educational base for the course. This may include:

- Theory notebooks on design philosophy, loads, and limit states
- Class-based Python tools for flexure, axial load, shear, and slab design
- Initial numerical examples
- Progressive organization of notebooks and supporting files

As the semester advances, more files and examples will be added.

## Recommended Workflow for Students

For each class session, students are encouraged to follow the workflow below:

1. Open the repository folder in VS Code
2. Open the integrated Command Prompt terminal
3. Activate the virtual environment
4. Verify that the correct Python interpreter has been selected
5. Open the corresponding notebook or Python file
6. Run the examples step by step
7. Modify the examples progressively as discussed in class
8. Save the updated work in an organized manner

This workflow helps maintain consistency during the semester and reduces the most common installation and execution errors.

## Updating the Repository

Since the repository will be updated progressively during the semester, students should regularly download the latest changes from GitHub.

### Step 1. Open the terminal

Open **Command Prompt** or the **integrated terminal in VS Code**.

### Step 2. Move into the repository folder
```bash
    cd Repo_ConcreteII_Desing
```
### Step 3. Activate the virtual environment

If students are using **Command Prompt**, run:
```bash
    venv\Scripts\activate
```
### Step 4. Pull the latest changes
```bash
    git pull
```
This command downloads and merges the most recent changes from the remote repository into the local copy.

### Recommendation

Students are encouraged to run `git pull` before starting each class session in order to work with the latest version of the repository.

## Summary of the Main Installation and Update Commands

### First-time installation
```bash
    git clone https://github.com/Normando1945/Repo_ConcreteII_Desing.git
    cd Repo_ConcreteII_Desing
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    pip install -e .
```
### Regular update before class
```bash
    cd Repo_ConcreteII_Desing
    venv\Scripts\activate
    git pull
```
## Additional Notes

- If Git is not recognized in the terminal, it must be installed and added correctly to the system path.
- If Python is not recognized in the terminal, verify that Python was installed correctly and added to the system path.
- If a notebook does not run, first verify that the correct Python interpreter and Jupyter kernel have been selected.
- It is recommended that all package installations be done only after activating the virtual environment.
- Students should avoid installing packages globally unless it is absolutely necessary.
- Since the repository is installed in editable mode, updates to the package files will be reflected directly without reinstalling the package in most cases.
- Because the repository is still under development, some folders or files may appear progressively during the semester.

## Important Note for Students

This repository is maintained exclusively by the course authors.

Students are expected to clone the repository and update their local copies during the semester. They should not modify the original online repository.

If students wish to experiment with the code, they are encouraged to do so in their local copies or in personal forks of the repository.

## How to Cite

If you use this repository in academic work, class projects, reports, or educational material, please cite it as follows.

### BibTeX

    @misc{celi2026concretedesignII,
      author       = {Celi Sánchez, Carlos Andrés and Mora Bowen, Nicolás and Baquero, Juan Sebastián},
      title        = {Reinforced Concrete Design II: Educational Repository for Concrete Design and Structural Engineering},
      year         = {2026},
      publisher    = {GitHub},
      journal      = {GitHub repository},
      howpublished = {\url{https://github.com/Normando1945/Repo_ConcreteII_Desing}}
    }

### APA (7th Edition)

Celi Sánchez, C. A., Mora Bowen, N., & Baquero, J. S. (2026). *Reinforced Concrete Design II: Educational Repository for Concrete Design and Structural Engineering* [Structural Engineering]. GitHub. https://github.com/Normando1945/Repo_ConcreteII_Desing

## License
<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
</p>

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

This repository is maintained by the authors as the official course repository for **Reinforced Concrete Design II**.

Students are encouraged to use the repository, report bugs, and suggest improvements whenever necessary. Nevertheless, the official development and organization of the repository remain under the supervision of the authors.

Suggestions for improvement may be shared through issues or pull requests, which will be reviewed before any change is incorporated into the repository.

## General Recommendation

Students are encouraged to keep this repository updated throughout the semester and use it as the main reference point for class notes, numerical examples, design criteria, and the progressive development of reinforced-concrete design tools and concepts.
