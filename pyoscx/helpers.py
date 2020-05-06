import xml.etree.ElementTree as ET
import xml.dom.minidom as mini

def prettyprint(element):
    """ prints the element to the commandline

        Parameters
        ----------
            element (Element): element to print

    """
    rough = ET.tostring(element,'utf-8')
    reparsed = mini.parseString(rough)
    print(reparsed.toprettyxml(indent="\t"))

def printToFile(element,filename,prettyprint=True):
    """ prints the element to a xml file

        Parameters
        ----------
            element (Element): element to print

            filename (str): file to save to

            prettyprint (bool): pretty or "ugly" print

    """
    if prettyprint:    
        rough = ET.tostring(element,'utf-8')
        reparsed = mini.parseString(rough)
        towrite = reparsed.toprettyxml(indent="\t")
        with open(filename,"w") as file_handle:
            file_handle.write(towrite)
    else:
        tree = ET.ElementTree(element)
        with open(filename,"wb") as file_handle:
            tree.write(file_handle)