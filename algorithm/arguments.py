# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

from argparse import ArgumentParser

class Arguments:
    def __init__(self, title: str, description: str = None) -> None:
        self.add = False
        self.parser = ArgumentParser(prog=title, description='description: '+description)
        self.parser.format_help()
        self.options = []
        self.groups = {}

    def __check__(self) -> None:
        if not self.add:
            raise Exception('No arguments found...! *_*')
    
    def add_group(self, name: str, title: str, decription: str) -> None: self.groups[name] = self.parser.add_argument_group(title, decription)

    def add_argument(self, shorter: str, longer: str, type: any, description: str, optional: bool = False, length: int = 1, group: str = None, default=None) -> None:
        if optional:
            description += ' (optional)'
            self.options.append(longer)
        if default:
            description += ' (default=%s)' % default
        if length <= 0:
            length = '+'
        if group:
            opj = self.groups[group]
        else:
            opj = self.parser
        opj.add_argument('-' + shorter, '--' + longer, nargs=length, type=type, help=description, default=default)
        if not self.add:
            self.add = True

    def get_argument(self, longer: str) -> list:
        arg = self.get_arguments()[longer]
        if arg != None and arg.__len__() == 1:
            arg = arg[0]
        return arg

    def get_arguments(self) -> dict:
        self.__check__()
        dic = {}
        for arg in self.parser.parse_args()._get_kwargs():
            dic[arg[0]] = arg[1]
        return dic
    
    def check_none(self) -> str:
        dic = self.get_arguments()
        for i in dic:
            if not dic[i]:
                if not i in self.options:
                    return i
        return None
    
    def help_none(self, close: bool = True) -> None:
        if self.check_none():
            self.print_help()
            if close:
                exit()
    
    def print_help(self) -> None:
        self.parser.print_help()
        print('\nDevelopment by Mostafa Algorithm\n')
    
    def get_parser(self) -> ArgumentParser: return self.parser