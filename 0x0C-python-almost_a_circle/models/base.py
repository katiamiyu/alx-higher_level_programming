#!/usr/bin/python3
"""
contain a base class
"""
import csv
import json


class Base():
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing function
        Args
            id: id of created instance
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert list of dicts to a json string obj
        Args:
            list_dictionaries: list of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return str([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves json str repr of a list obj into file
        Args:
            cls: obj class
            list_objs: obj list
        """
        file_name = cls.__name__
        my_list = []
        if list_objs is None or list_objs == []:
            my_list = []
        else:
            for ele in list_objs:
                my_list.append(ele.to_dictionary())
        data = cls.to_json_string(my_list)
        with open(f"{file_name}.json", "w") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
        retreives obj from json str repr
        Args:
            json_string: json string repr of obj
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates instance of a class(obj)
        Args:
            cls: instance class
            dictionary: dictionary of  instance
        """
        name = cls.__name__
        if name == "Rectangle":
            rectangle = cls(5, 10)
            rectangle.update(**dictionary)
            return rectangle
        else:
            square = cls(2)
            square.update(**dictionary)
            return square

    @classmethod
    def load_from_file(cls):
        """
        return list of instances fron a file
        obj with json representation of those instances
        """
        instancelist = []
        name = cls.__name__
        try:
            with open(f"{name}.json") as f:
                mylist = cls.from_json_string(f.read())
                for ele in mylist:
                    instancelist.append(cls.create(**ele))
                return instancelist
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Stores rectangle and square objs to .csv file

        Args:
           list_objs (list): A list of Square or Rectangle obj.
        '''
        name = cls.__name__
        with open(f"{name}.csv", 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            if list_objs is None or list_objs == []:
                csv_writer.writerow("")
            else:
                for obj in list_objs:
                    if name == "Square":
                        csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])
                    elif name == "Rectangle":
                        csv_writer.writerow([obj.id, obj.width,
                                             obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''Retrieves data from .csv file
            returns a list of Square or 
            Rectangle Objects
        '''
        result = []
        name = cls.__name__
        with open(f"{name}.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if name == "Square":
                    result.append(cls.create(id=int(row[0]), size=int(row[1]),
                                             x=int(row[2]), y=int(row[3])))
                elif name == "Rectangle":
                    result.append(cls.create(id=int(row[0]), width=int(row[1]),
                                             height=int(row[2]), x=int(row[3]),
                                             y=int(row[4])))
        return result
