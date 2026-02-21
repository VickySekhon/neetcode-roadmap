class HTML:
     CLOSED_TAGS={"<p>":"</p>"}
     
     def __init__(self, tag, text="", className=None, id=None, ariaLabel=None):
          self.tag = tag
          self.text = text
          self.className = className
          self.id = id
          self.ariaLabel = ariaLabel
     
     def addText(self, text):
          self.text = text
          
     def addClassName(self, className):
          self.className = className
     
     def __str__(self):
          if self.className and self.tag in self.CLOSED_TAGS: return f"class: {self.className}\n{self.tag}{self.text}{self.CLOSED_TAGS[self.tag]}"
          if self.tag in self.CLOSED_TAGS:
               return f"{self.tag}{self.text}{self.CLOSED_TAGS[self.tag]}"
          return f"{self.tag}{self.text}"

class CSS:
     VALID_CSS_PROPERTIES = [
    "color", "background-color", "font-size", "font-weight", "margin", 
    "padding", "border", "width", "height", "display", "position",
    "top", "left", "right", "bottom", "z-index", "opacity", "visibility",
    "overflow", "text-align", "line-height", "letter-spacing", "word-spacing",
    "text-decoration", "text-transform", "vertical-align", "white-space",
    "float", "clear", "box-sizing", "border-radius", "box-shadow",
    "text-shadow", "transform", "transition", "animation", "flex",
    "flex-direction", "justify-content", "align-items", "grid",
    "grid-template-columns", "grid-template-rows", "cursor"]
     
     def __init__(self, html, styles={}):
          self.html = html
          self.styles = styles
     
     def addStyle(self, key, value):
          if not key in self.VALID_CSS_PROPERTIES:
               print(f"Invalid css style")
               return
          
          if key in self.styles:
               existingValue = self.styles[key]
               print(f"Style: {key} is already set to {existingValue}. Would you like to overwrite it?")
               overwrite = input("Y or N") 
               if overwrite == "Y":
                    self.styles[key] = value
                    print(f"Successfully overwrote style")
               else:
                    print(f"Did not overwrite style")
          else:
               self.styles[key] = value
     
     def _assert_style_exists(self, key):
          assert key in self.styles, f"Style: {key} does not exist on tag. You must add it before calling this function."

     def removeStyle(self, key):
          self._assert_style_exists(key)
          del self.styles[key]
          return f"Style successfully removed..."
     
     def modifyStyle(self, key, newValue):
          self._assert_style_exists(key)
          self.styles[key] = newValue
          return f"Class: {key} is now set to {newValue}"
     
     def removeAllStyles(self):
          self.styles = {}
     
     def stylesActive(self) -> int:
          return len(self.styles)
          
     def __str__(self):
          return f"{self.html}\nStyles: {self.styles}"

html = HTML("<p>")
html.addText("hello vicky!")
html.addClassName("my-text")
css = CSS(html)
css.addStyle("color", "red")
print(css)
print(css.modifyStyle("color", "blue"))
print(css)
#print(css.removeStyle("color"))
#print(css.removeStyle("background-color"))