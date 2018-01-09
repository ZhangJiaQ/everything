     

class DiagramFactory:
    
    @classmethod   #类方法 ， 会返回类
    def make_diagram(Class, width, heigh):
        return Class.Diagram(width, heigh)
    
    @classmethod    
    def make_rectangle(Class, x, y, width, heigh, fill="white", stroke="black")
        return Class.Rectangle(x, y, width, heigh, fill, stroke)
    
    @classmethod
    def make_text(self, x, y, text, fontsize=12):
        return Class.Text(x, y, text, fontsize)
        

class SvgDiagramFactory(DiagramFactory):
    
    SVG_TEXT = """<text x="{x}" y="{y}"  text-anchor="left" \
    font-family="sans-serif" font-size="{fontsize}">{text}</text>"""
    SVG_SCALE = 20  
        
    def make_diagram(self, width, heigh):
        return SvgDiagram(width, heigh)
        
    class Text:
        def __init__(self, x, y, text, fontsize):
            x *= SVG_SCALE
            y *= SVG_SCALE
            fontsize *= SvgDiagramFactory.SVG_SCALE // 10
            self.svg = SvgDiagramFactory.SVG_TEXT.format(**locals())
    

class Text：
    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]
        
        
class Diagram:
    """"""
    def add(self, component):
        for y, row in enumerate(component.rows):
            for x, row in enumerate(roww):
                self.diagram[y+component.y][x+component.x] = char
                
class SvgDiagram:
    """"""
    def add(self, component):
        self.diagram.append(component.svg)
                
                

        
        

def create_diagram():
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, 'yellow')
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


def main():
    ''''''
    txtDiagram = create_diagram(DiagramFactory)
    txtDiagram.save(textFilename)
    
    svgDiagram = create_diagram(SvgDiagramFactory)
    svgDiagram.save(svgFilename)
    