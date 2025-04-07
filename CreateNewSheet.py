import os
import shutil

################## CONFIG ##################
# If you change the name of the script please change the value of nameOfScript to match the full name.
nameOfScript = "CreateNewSheet.py"
pdfNamePrefix = "Sheet"
pdfNameSuffix = "_Name"
sheetDirPrefix = "Sheet"
############################################

def getNameOfPDF(sheetNumber: int) -> str:
    return pdfNamePrefix + str(sheetNumber) + pdfNameSuffix

def commitAndPush(path: str) -> None:
    os.system("git add .")
    os.system(f"git commit -m \"Initial commit for {path}\"")
    os.system("git push")

def getAbsolutePathOfScript() -> str: 
    scriptAbsPath = __file__
    lenOfScriptName = (-len(nameOfScript))
    scriptAbsPath = scriptAbsPath[:lenOfScriptName]
    return scriptAbsPath

def getNextSheetNumber() -> int: 
    sheetNumber = 1
    for i in range(1, 20):
        path = sheetDirPrefix + str(i)
        sheetNumber = os.listdir().count(path) + sheetNumber
    return sheetNumber

def renameFile(old_name, new_name) -> None:
    try:
        os.rename(old_name, new_name)
        print(f"File {old_name} renamed to {new_name} successfully.")
    except FileNotFoundError:
        print(f"Error: File {old_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def copyFile(source: str, destination: str) -> None:
    try:
        # Copy the file to the destination
        shutil.copy(source, destination)
        print(f"File '{source}' copied to '{destination}' successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission denied to copy the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return

def createNewSheetDir(sheetNumber: int) -> str:
    newSheetDir = sheetDirPrefix + str(sheetNumber)
    os.mkdir(newSheetDir)
    return newSheetDir

def getPath(dirs: list[str]) -> str: 
    return os.sep.join(dirs)

def copyTemplate(dst: str, sheetNumber:int) -> None:
    pathStyles = getPath([dst ,"styles"])
    pathFigures = getPath([dst, "figures"])

    os.mkdir(pathStyles)
    os.mkdir(pathFigures)
    
    copyFile(getPath(["LatexTemplate","styles","Packages.tex"]), pathStyles)
    copyFile(getPath(["LatexTemplate","styles","FormatAndHeader.tex"]), pathStyles)

    copyFile(getPath(["LaTeXTemplate","template.tex"]), getPath([dst]))
    renameFile(getPath([dst,"template.tex"]), getPath([dst, getNameOfPDF(sheetNumber) + ".tex"]))
    return


os.chdir(getAbsolutePathOfScript())
os.system("git pull")

newSheetNumber = getNextSheetNumber()
newSheetDir = createNewSheetDir(newSheetNumber)
copyTemplate(newSheetDir, newSheetNumber)

done = input("Do you want to commit and push all changes so far? (y/n): ")
if (done == "y"):
    commitAndPush(newSheetDir)
done = input("Done! Press any key to exit")