# This module contains the datastructures for metadata extraction

class dc_elems:
    def __init__(self):
        print("Creating new dc instance")
        self.dublin_core_elements = {}

    def _fill_metadata_(self):
        pass

class qp_met(dc_elems):

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