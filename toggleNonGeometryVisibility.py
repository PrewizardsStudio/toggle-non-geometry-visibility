moduleName = 'toggleNonGeometryVisibility'
moduleNameLong = 'Toggle non-geometry visibility in active panel'
moduleUrl = 'https://github.com/PrewizardsStudio/toggle-non-geometry-visibility'
moduleIconUrl = 'https://github.com/PrewizardsStudio/toggle-non-geometry-visibility/blob/main/toggleNonGeometryVisibility.png?raw=true'
moduleCommand = """
def setNonGeometryVisibility(visibility='True|False|toggle', targetModelPanel = 'active'):
    if targetModelPanel == 'active':    
        cmds.getPanel( withFocus=True )
    if visibility == 'toggle':
        visibility = not cmds.modelEditor (targetModelPanel, query = True, locators = True)
    cmds.modelEditor (targetModelPanel, edit = True, locators = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, pivots = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, joints = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, cameras = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, ikHandles = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, lights = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, nurbsCurves = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, manipulators = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, grid = visibility)
    #cmds.modelEditor (targetModelPanel, edit = True, hud = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, sel = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, handles = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, dimensions = visibility)
    cmds.modelEditor (targetModelPanel, edit = True, motionTrails = visibility)
setNonGeometryVisibility(visibility='toggle', targetModelPanel = 'active')
"""

def onMayaDroppedPythonFile(args):
    import sys
    del sys.modules[moduleName]
    installScript()
    
def installScript():
    import requests, os
    import maya.mel as mel
    import maya.cmds as cmds

    iconImageName = moduleIconUrl.split('/')[-1].replace('?raw=true','')

    # Get current maya version
    version = cmds.about(version=True)

    # Download Icon
    appPath = os.environ['MAYA_APP_DIR']
    iconPath = os.path.join(appPath, version, "prefs/icons", iconImageName)

    if not os.path.exists(iconPath):
        result = requests.get(moduleIconUrl, allow_redirects=True)
        open(iconPath, 'wb').write(result.content)  

    # Add to current shelf
    topShelf = mel.eval('$nul = $gShelfTopLevel')
    currentShelf = cmds.tabLayout(topShelf, q=1, st=1)
    cmds.shelfButton(parent=currentShelf, image=iconPath, command=moduleCommand, label=moduleNameLong, annotation=moduleNameLong)