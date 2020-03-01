import yaml


class TestYAML:
    def test_yaml(self):
        print(yaml.load("""
        
        - 
            - 1
            - 2
            - 3
        -
            - 4
            - 5 
            - 6
        """))
