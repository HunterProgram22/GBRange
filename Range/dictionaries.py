# Form and Model Dictionaries
from .models import Woods_Technical, Hybrids_Technical, Irons_Technical, \
    Wedges_Technical, Chipping_Technical, Putting_Technical, Woods_Experimental, \
    Wedges_Experimental, Putting_Experimental, Irons_Experimental, \
    Hybrids_Experimental, Chipping_Experimental
from .forms import Woods_Test_Form, Woods_Technical_Form, Hybrids_Technical_Form, \
    Irons_Technical_Form, Wedges_Technical_Form, Chipping_Technical_Form, \
    Putting_Technical_Form, Woods_Experimental_Form, Wedges_Experimental_Form, \
    Putting_Experimental_Form, Irons_Experimental_Form, Hybrids_Experimental_Form, \
    Chipping_Experimental_Form

form_names_dict = {'Woods_Experimental_Form':Woods_Experimental_Form,
                   'Woods_Technical_Form':Woods_Technical_Form,
                   'Hybrids_Experimental_Form':Hybrids_Experimental_Form,
                   'Hybrids_Technical_Form':Hybrids_Technical_Form,
                   'Irons_Experimental_Form':Irons_Experimental_Form,
                   'Irons_Technical_Form':Irons_Technical_Form,
                   'Wedges_Experimental_Form':Wedges_Experimental_Form,
                   'Wedges_Technical_Form':Wedges_Technical_Form,
                   'Chipping_Experimental_Form':Chipping_Experimental_Form,
                   'Chipping_Technical_Form':Chipping_Technical_Form,
                   'Putting_Experimental_Form':Putting_Experimental_Form,
                   'Putting_Technical_Form':Putting_Technical_Form,}

model_names_dict = {'Woods_Experimental':Woods_Experimental,
                    'Woods_Technical':Woods_Technical,
                    'Hybrids_Experimental':Hybrids_Experimental,
                    'Hybrids_Technical':Hybrids_Technical,
                    'Irons_Experimental':Irons_Experimental,
                    'Irons_Technical':Irons_Technical,
                    'Wedges_Experimental':Wedges_Experimental,
                    'Wedges_Technical':Wedges_Technical,
                    'Chipping_Experimental':Chipping_Experimental,
                    'Chipping_Technical':Chipping_Technical,
                    'Putting_Experimental':Putting_Experimental,
                    'Putting_Technical':Putting_Technical,}
