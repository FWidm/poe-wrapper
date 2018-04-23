from src.util.regex import strip_translation_prefix


class Item:
    def __init__(self, **kwargs):
        self.verified = kwargs.get('verified')
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.ilvl = kwargs.get('ilvl')
        self.icon = kwargs.get('icon')
        self.league = kwargs.get('league')
        self.id = kwargs.get('id')
        # todo parse into own objects[group, attrib{s,d,i},sColour{R,G,B}
        self.sockets = kwargs.get('sockets')
        self.name = strip_translation_prefix(kwargs.get('name'))
        self.type = strip_translation_prefix(kwargs.get('type_line'))
        self.identified = kwargs.get('identified')
        # various properties such as quality names, values[], displayMode,type
        self.properties = kwargs.get('properties')
        self.requirements = kwargs.get('requirements')
        # string array
        self.explicit_mods = kwargs.get('explicit_mods')
        self.flavour_text = kwargs.get('flavour_text')
        self.frame_type = kwargs.get('frame_type')
        self.category = kwargs.get('category')
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.slot = kwargs.get('slot')
        # list of items
        self.socketed_items = kwargs.get('socketed_items')
        self.implicit_mods = kwargs.get('implicit_mods')
        self.type_line = kwargs.get('type_line')

    @staticmethod
    def from_dict(item_dict):
        item = Item(
            verified=item_dict.get('verified'),
            width=item_dict.get('w'),
            height=item_dict.get('h'),
            ilvl=item_dict.get('ilvl'),
            icon=item_dict.get('icon'),
            league=item_dict.get('league'),
            id=item_dict.get('id'),
            sockets=item_dict.get('sockets'),
            name=item_dict.get('name'),
            type_line=item_dict.get('typeLine'),
            identified=item_dict.get('identified'),
            properties=item_dict.get('properties'),
            requirements=item_dict.get('requirements'),
            explicit_mods=item_dict.get('explicitMods'),
            flavour_text=item_dict.get('flavourText'),
            frame_type=item_dict.get('frameType'),
            category=item_dict.get('category'),
            x=item_dict.get('x'),
            y=item_dict.get('y'),
            slot=item_dict.get('inventoryId'),
            socketed_items=item_dict.get('socketedItems'),
            implicit_mods=item_dict.get('implicitMods'),

        )
        return item

    def get_linked_sockets(self) -> dict:
        """
        Get the links of an item in the form of a dict with socket groups as key and a list of characters as socket colors
        :return: dictionary in the style of {0:[RRB],1:[BBB]} for an item with 6 sockets and 2 three links.
        """
        links = {}
        if not self.sockets:
            return links

        for socket in self.sockets:
            group = socket['group']
            if not links.get(group):
                links[group] = []
            links[group].append(socket['sColour'])
        return links

    def get_gems(self):
        """
        Get all socketed gems in the correct order.
        :return: List[Item] list of socketed gems in this item
        """
        gems = []
        for raw_gem in self.socketed_items:
            gem = Item.from_dict(raw_gem)
            gems.append(gem)
        return gems

    def __repr__(self):
        ret = self.name
        if self.name=="":
            ret = self.type
        if self.type=="":
            ret = self.type_line
        return ret

    def __eq__(self, other):
        """
        An item is equal as long as it is of the instance "Item", has the same name, frame type, explicit and implicit
        mods and the frame type matches
        :param other: Item to compare this with
        :return: True if equal in the specified way
        """
        if other == None or not isinstance(other,Item):
            return False
        if self.name != other.name or self.type != other.type or self.type_line != other.type_line:
            return False
        if self.get_linked_sockets() != other.get_linked_sockets():
            print(self.get_linked_sockets(), other.get_linked_sockets())

            return False
        if self.frame_type != other.frame_type:
            return False
        if self.explicit_mods != other.explicit_mods:
            print(self.explicit_mods,other.explicit_mods)
            return False

        if self.implicit_mods != other.implicit_mods:
            #todo: bubble up the changes to save it in the report
            print(self.implicit_mods,other.implicit_mods)

            return False
        return True


    def __ne__(self, other):
        return not self.__eq__(other)
