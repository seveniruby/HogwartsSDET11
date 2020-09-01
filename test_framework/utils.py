import yaml


class Utils:
    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            yaml_data=yaml.safe_load(f)
            params=yaml_data['params']
            keys = set()
            values=[]
            if isinstance(params, list):
                for row in params:
                    if isinstance(row, dict):
                        for key in row.keys():
                            keys.add(key)
                            values.append(list(row.values())[0])
            var_names=','.join(keys)

            res={'keys': var_names, 'values': values}
            print(res)

            return res