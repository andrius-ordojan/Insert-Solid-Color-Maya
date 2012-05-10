from pymel.core import *
import pymel.core.nodetypes as nt
import pymel.core.datatypes as dt

includeGammaCorrect = True
gammaCorrectValue = (0.455, 0.455, 0.455)

selectedMaterials = selected(materials = True)

for material in selectedMaterials:
    if material.hasAttr('color') is False or material.color.isConnected():
        continue
    
    materialName = material.name()
    
    originalColor = dt.Color(material.getColor())
          
    ramp = nt.Ramp(name = '%s_Color' % materialName)
    
    for colorEntry in ramp.colorEntryList:
        colorEntry.remove()
    
    ramp.colorEntryList[0].position.set(0.0)
    ramp.colorEntryList[0].color.set(originalColor)
    
    if includeGammaCorrect:
        gammaCorrect = nt.GammaCorrect(name = '%s_Color_GammaCorrect' % materialName)
        gammaCorrect.gamma.set(gammaCorrectValue)
        
        ramp.outColor.connect(gammaCorrect.value)
        gammaCorrect.outValue.connect(material.color)
    else:
        ramp.outColor.connect(material.color)
