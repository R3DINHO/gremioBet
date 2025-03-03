from django import forms

class ImageRadioSelect(forms.RadioSelect):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        for option in self.choices:
            option_value, option_label = option
            img_html = f'<img src="/static/img/fotosPerfil/{option_value}" width="50" height="50" />'
            option_html = f'<label>{img_html} <input type="radio" name="{name}" value="{option_value}" {attrs} />{option_label}</label>'
            output.append(option_html)
        return '\n'.join(output)
