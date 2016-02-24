# This module contains the datastructures for metadata extraction

from pprintpp import pprint

class dc_elems:
    def __init__(self):
        print("Creating new dc instance")
        self.metadata_elements = {}

    def _init_metadata_(self):
        pass

class qp_metadata(dc_elems):
    def __init__(self, publisher, language="English"):
        super().__init__()
        self._init_metadata_(publisher, language)

    def _init_metadata_(self, publisher, language):
        self._add_metadata_element("publisher", publisher)
        self._add_metadata_element("language", language)

    def _add_metadata_element(self, metadata_property, value):
        '''metadata_property has to be a string'''
        self.metadata_elements[metadata_property] = value

    def print_metadata_dict(self):
        pprint(self.metadata_elements)

        '''
            'contributor': {'author' : (),
             				'illustrator' : (),
             				'editor' : (),
                            'none' : ()
                                    },
             'title':(),
             'creator': (), # creator to be merged into author in final xml
             'subject': { 'lcc' : (),
                        'ddc' : (),
                        'none' : ()},
             'description': {
                              'abstract' : (),
                              'toc' : (),
                              'none' : ()
                              },
             'publisher':(),

             'date': {
             			'created' : (),
             			'accessioned' : (),
             			'copyright' : (),
                              'none' : ()
             			},
             'type':(),
             'format': {
             			'extent' : (),
             			'mimetype' : (),
                              'none' : ()
             			},
             'identifier': {
             				'uri' : (),
             				'isbn' : (),
             				'issn' : (),
             				'citation' : (),
                                    'none' : ()
             				},
             'source':(),
             'language':(),
             'relation': {    
                              'ispartof' : (),
                              'ispartofseries' : (),
                              'haspart' : (),
                              'isrefencedby' : (),
                              'refernces' : ()
                              },
             'coverage':(),
             'rights':()
        }
        '''


#synonymous = {
#      'illustrator' : ("graphics", "cover",)
#}

# headers

#first = ["author","editor","illustrator","graphics","cover","coordinator","indexer","proofreader","reviewer"]
#headers = {
#      '1' : first
#}