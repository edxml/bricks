from edxml.ontology import Ontology
from lxml import etree

from generic.python.edxml_bricks.generic import GenericBrick
from geography.python.edxml_bricks.geography import GeoBrick
from computing.python.edxml_bricks.computing.generic import ComputingBrick
from computing.python.edxml_bricks.computing.email import EmailBrick
from computing.python.edxml_bricks.computing.files import FilesBrick
from forensics.python.edxml_bricks.computing.forensics.generic import ForensicsBrick
from forensics.python.edxml_bricks.computing.forensics.platforms.windows import WindowsBrick
from security.python.edxml_bricks.computing.security import SecurityBrick
from security.python.edxml_bricks.computing.security import CryptoBrick
from networking.python.edxml_bricks.computing.networking.generic import NetworkingBrick
from networking.python.edxml_bricks.computing.networking.http import HttpBrick
from finance.python.edxml_bricks.finance.generic import FinanceBrick
from finance.python.edxml_bricks.finance.currencies.common import CommonCurrenciesBrick
from finance.python.edxml_bricks.finance.currencies.all import AllCurrenciesBrick


def brick_object_type_names(brick, url=None):
    ontology = Ontology()

    rst_lines = []
    for object_type in brick.generate_object_types(ontology):
        entry = object_type.get_name()
        if url:
            entry = f"`{entry} <{url}#{entry.replace('.', '')}>`"
        rst_lines.append(f"- {entry}_")

    return rst_lines


def brick_object_types_details(brick):
    ontology = Ontology()

    rst = ''
    for object_type in brick.generate_object_types(ontology):
        rst += object_type_details(object_type) + '\n'

    return rst


def object_type_details(object_type):
    rst = ''
    xml = etree.tostring(object_type.generate_xml(), pretty_print=True) \
        .decode() \
        .replace('" ', '"\n               ')
    rst += object_type.get_name() + '\n' + '-' * len(object_type.get_name()) + '\n'
    rst += f"*{object_type.get_description()}*\n\n"
    rst += '.. code-block:: xml\n\n  ' + xml
    return rst


def brick_concept_names(brick, url=None):
    ontology = Ontology()

    rst_lines = []
    for concept in brick.generate_concepts(ontology):
        entry = concept.get_name()
        if url:
            entry = f"`{entry} <{url}#{entry.replace('.', '')}>`"
        rst_lines.append(f"- {entry}_")

    return rst_lines


def brick_concepts_details(brick):
    ontology = Ontology()

    rst = ''
    for concept in brick.generate_concepts(ontology):
        rst += concept_details(concept) + '\n'

    return rst


def concept_details(concept):
    rst = ''
    xml = etree.tostring(concept.generate_xml(), pretty_print=True) \
        .decode() \
        .replace('" ', '"\n           ')
    rst += concept.get_name() + '\n' + '-' * len(concept.get_name()) + '\n'
    rst += f"*{concept.get_description()}*\n\n"
    rst += '.. code-block:: xml\n\n  ' + xml
    return rst


paths_bricks = {
    'generic': [GenericBrick],
    'geography': [GeoBrick],
    'computing': [ComputingBrick, EmailBrick, FilesBrick],
    'forensics': [ForensicsBrick, WindowsBrick],
    'security': [SecurityBrick, CryptoBrick],
    'networking': [NetworkingBrick, HttpBrick],
    'finance': [FinanceBrick, CommonCurrenciesBrick, AllCurrenciesBrick]
}

with open('index.rst', 'w') as index:
    object_type_names = []
    for path, bricks in paths_bricks.items():
        for brick in bricks:
            object_type_names.extend(brick_object_type_names(brick(), url=f"{path}/index.rst"))

    if object_type_names:
        index.write('Object Types\n')
        index.write('------------\n')
        index.write('\n'.join(sorted(object_type_names)))
        index.write('\n\n')

    concept_names = []
    for path, bricks in paths_bricks.items():
        for brick in bricks:
            concept_names.extend(brick_concept_names(brick(), url=f"{path}/index.rst"))

    if concept_names:
        index.write('Concepts\n')
        index.write('--------\n')
        index.write('\n'.join(sorted(concept_names)))
        index.write('\n')

for path, bricks in paths_bricks.items():
    with open(f"{path}/index.rst", 'w') as brick_index:
        brick_index.write('********\n')
        brick_index.write('Contents\n')
        brick_index.write('********\n\n')
        brick_index.write('An overview of the ontology elements is provided below.\n\n')

        have_concepts = False
        have_object_types = False

        for brick in bricks:
            brick_index.write(brick.__name__ + '\n')
            brick_index.write('=' * len(brick.__name__) + '\n')
            if brick_object_type_names(brick()):
                have_object_types = True
                # Write sorted references, ignoring the trailing underscore.
                brick_index.write('Object types:\n\n')
                brick_index.write(
                    '\n'.join(sorted(brick_object_type_names(brick()), key=lambda item: item[:-1])) + '\n\n'
                )
            if brick_concept_names(brick()):
                have_concepts = True
                # Write sorted references, ignoring the trailing underscore.
                brick_index.write('Concepts:\n\n')
                brick_index.write(
                    '\n'.join(sorted(brick_concept_names(brick()), key=lambda item: item[:-1])) + '\n\n'
                )
        brick_index.write('\n\n')
        brick_index.write('***********\n')
        brick_index.write('Definitions\n')
        brick_index.write('***********\n\n')
        if have_object_types:
            brick_index.write('Object Types\n')
            brick_index.write('============\n\n')
            for brick in bricks:
                brick_index.write(brick_object_types_details(brick()))
        if have_concepts:
            brick_index.write('Concepts\n')
            brick_index.write('========\n\n')
            for brick in bricks:
                brick_index.write(brick_concepts_details(brick()))
