import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test_1():
    _exec_notebook('01_Jupyter.ipynb')


def test_2():
    _exec_notebook('02_Pandas.ipynb')


def test_3():
    _exec_notebook('03_Scikit_Learn.ipynb')


def test_4():
    _exec_notebook('04_Keras.ipynb')


def test_5():
    _exec_notebook('05_Test_your_skills.ipynb')


soldir = "solutions_do_not_open/are_you_really_sure/are_you_really_really_sure/"


def test_2_sol():
    _exec_notebook(soldir+'02_Pandas_solution.ipynb')


def test_3_sol():
    _exec_notebook(soldir+'03_Scikit_Learn_solution.ipynb')


def test_4_sol():
    _exec_notebook(soldir+'04_Keras_solution.ipynb')


def test_5_sol():
    _exec_notebook(soldir+'05_Test_your_skills_solution.ipynb')