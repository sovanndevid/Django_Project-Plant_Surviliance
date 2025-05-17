from dataclasses import dataclass
from typing import List, Dict

@dataclass
class PestDisease:
    id: int
    name: str  # name of pest/disease
    scientific_name: str
    description: str
    image_url: str
    image_reference: str
    symptoms: List[str]
    prevention: List[str]
    treatment: List[str]

    def to_dict(self) -> Dict[str, str]:
        """Convert PestDisease instance to dictionary"""
        return {
            "id": str(self.id),
            "name": self.name,
            "scientific_name": self.scientific_name,
            "description": self.description,
            "image_url": self.image_url,
            "image_reference": self.image_reference,
            "symptoms": self.symptoms,
            "prevention": self.prevention,
            "treatment": self.treatment,
        }

def get_pests_list() -> List[PestDisease]:
    """Returns list of PestDisease instances"""
    return [
        PestDisease(
            id='1',
            name="Anthracnose",
            scientific_name="Collectotrichum glorosporioides",
            description="One of the most serious fungal disease of mangoes worldwide. It mostly affects the areas where it rains during the mango flowering and fruit stages.",
            image_url="/images/_anthracnose.jpg",
            image_reference="https://nt.gov.au/industry/agriculture/food-crops-plants-and-quarantine/fruit-crops/mango/pests-and-diseases",
            symptoms=[
                "This fungus causes black spots on leaves, they are tan to dark brown in color."
                "Then the spots tend to enlarge and it sunkens with dark margins."
                "When the newly formed fruit gets affected with Anthracnose it causes rotting and premature dropping of the fruit."
            ],
            prevention=[
                "Post-harvest treatments are available for control of Anthracnose in mango fruit."
                "Ensuring regular spraying of trees from flowering time onwards with mancozeb(agricultural fungicide) but after 14 days of harvest."
                "Hot water dips to control fruit flies will also control anthracnose and stem end rots."
            ],
            treatment=[
                "Regular pruning of dead or infected plant parts to reduce the risk of further infection."
                "Using fungicides that are specifically for anthracnose and using it at correct times."
            ],
        ),
        PestDisease(
            id='2',
            name="Mango scab",
            scientific_name="Denticularia maniferae",
            description="This is a fungus that causes black spots on new fruits. It was first described in 1943 from specimens from Cuba and Florida but now it is found in most of the mango growing areas around the world.",
            image_url="/images/mango-scab-mango-1557912424.jpg",
            image_reference="https://apps.lucidcentral.org/pppw_v10/text/web_full/entities/mango_bacterial_black_spot_213.htm",
            symptoms=[
                "Some symptoms can be confused with physical or insect injury or infection by other disease."
                "Mostly noticeable symptoms are on the fruits. When small black lesions form on newly-set fruit and the heavily affected fruit falls off the tree."
                "In leaves, common symptoms are brrown spots with haloes, edge lesions, corky lesions on the lower surface of leaves and elongated dark lesions along main veins under the leaves."
            ],
            prevention=[
                "Removing fallen leaves and fruits to reduce fungal sores in the orchard."
                "Ensuring proper tree spacing to improve air circulation and reduce humidity."
            ],
            treatment=[
                "Since, mango scab is recently identified in Australia, treatment measures are being developed and recommendations may change with time as we gain more experiences."
                "For orchards, copper sprays should be applied as soon as the flower panicles starts to emerge and continue it at two to three intervals till the fruit has half grown."
                "Furthermore, weekly sprays of copper fungicides may be required in mango nurseries to prevent defoliation, especially in wet weather."
            ],

        ),
        PestDisease(
            id='3',
            name="Mango scale",
            scientific_name="Aulacaspis tubercularis",
            description="Mango scale is present all year round, with overlapping generations throught the year.",
            image_url="/images/mango_scale.jpg",
            image_reference="https://daf.nt.gov.au/__data/assets/pdf_file/0018/228015/mango_scale_management_poster.pdf",
            symptoms=[
                "Parts of leaves start to turn yellow in color."
                "As the insect come to plant sap, they excrete sticky sugary substance called 'honeydew' whcih then coats the stems, leaves and fruits."
            ],
            prevention=[
                "Most imporatnt one is regular monitoring of trees."
                "Promoting natural enemies such as ladybugs, parasitic wasps which feed on scale insects."
                "Triming and removing heavily infected branches and leaves."
            ],
            treatment=[
                "Applying chemicals only if monitoring shows significant live scale activity."
                "Spray of neem oil on affected areas to suffocate and kill scale insects during the early stages."
            ],
        ),
        PestDisease(
            id='4',
            name="Bacterial black spot",
            scientific_name="Xanthomonas campestris pv. mangiferae-indicae",
            description="Bacterial black spot was first found in 1981 in the NT and since then it has appeared in most areas where mangoes are grown in the Northen Territory.",
            image_url="/images/mango_bacterial_spot.jpg",
            image_reference="https://apps.lucidcentral.org/pppw_v10/text/web_full/entities/mango_bacterial_black_spot_213.htm",
            symptoms=[
                "Leaf spots are black and they tend to get angular in shape as they are confined by larger veins."
                "Twig and stem lesions are black and cracked."
                "Black scabby spots are formed on fruit with star shaped cracked within them."
            ],
            prevention=[
                "Using disease-free planting stock."
                "Prunning to remove infected branches and improve aeration within the tree."
                "Practice hygeine sterilisation of harvesting implements."
            ],
            treatment=[
                "Use of Manzate chemical to kill, not just prevent established blackspot."
            ],
        ),
        PestDisease(
            id='5',
            name="Fruit fly",
            scientific_name="Drosophila melanogaster",
            description="Major pest that lays eggs inside mango fruits.",
            image_url="/images/mango_fruit_fly.jpg",
            image_reference="https://industry.nt.gov.au/__data/assets/pdf_file/0004/1380748/mango-field-guide-part-4.pdf",
            symptoms=[
                "Female fruit flies lay eggs under fruit skin leaving small marks such as puncture marks."
                "Softening and rotting of infected mango fruits."
                "Presence of larvae inside the fruits causing internal rotting."
            ],
            prevention=[
                "Protecting young fruits or applying insecticides to prevent from egg-laying fruit flies."
                "Removal of fallen and infected fruits to disrupt the life cycle of fruit fly."
            ],
            treatment=[
                "Applying liqid food(protein) attractant to the foliage and trunk of trees and plant so that when the fruit fly start feeding on them the poisoned food will be ingested by them reducing the number in that area."
            ],
        ),
        PestDisease(
            id='6',
            name="Mango leafhoppers",
            scientific_name="Idioscopus nitidulus",
            description="Leafhoppers are 4-5mm long insects that lay eggs on leaves. They breed all year round but female lay more eggs and nymphs develop faster during the fruiting and flowering period.",
            image_url="/images/mango_leafhoppers.jpg",
            image_reference="https://daf.nt.gov.au/__data/assets/pdf_file/0007/1380742/mango-field-guide-part-1.pdf",
            symptoms=[
                "Leafhoppers are difficult to spot but it causes leaf curling and sooty mold due to sap feeding."
                "Impacting fruit production by 50 per cent or more if it is left untreated."
                "They increase more in numbers of flowering trees, damaging the flower stems through egg-laying and sap-sucking."
            ],
            prevention=[
                "Keeping wide distance between trees when planting."
                "Regular monitoring of orchids for nymphs and adults."
                "By not transfering the infected mango plants between orchards."
            ],
            treatment=[
                "Most important is using the recommended insecticides during early flowring."
                "Native lacewing larvae and other predators can help in controlling immature leafhoppers."
                "Controlling leafhoppers prior to flowering reduces the rick of pesticides affecting pollinators."
            ],
        ),
        PestDisease(
            id='7',
            name="Mango seed weevil",
            scientific_name="Sternocchetus mangiferae",
            description="Weevils attack mango seeds directly which tend to downgrade the fruit and severely reduce germination.",
            image_url="/images/seed_weevil.jpg",
            image_reference="https://industry.nt.gov.au/__data/assets/pdf_file/0004/1380748/mango-field-guide-part-4.pdf",
            symptoms=[
                "Unmanaged trees and fruit dumps are an additional source of weevil infection."
                "Adult weevils lay eggs on mango skin making tiny entry holes inside which then affects the fruit."
                "Infected mango may fall from the tree early due to internal damage."
            ],
            prevention=[
                "Check for adults undeer bark during winter."
                "Cut fruit and seeds at harvest to look for larvae."
                "Check for feeding damage on new flushes."
            ],
            treatment=[
                "Targeting emerging larvae on fruit with systemic chemicals."
                "Mulch the fallen fruits and prunings before weevils emerge."
                "Making sure to destroy rejected fruit and hence remove them from farms."
            ]
        )
    ]

def get_pests_dict() -> List[Dict[str, str]]:
    """Returns pests as list of dictionaries"""
    return [pest.to_dict() for pest in get_pests_list()]

if __name__ == "__main__":
    for pest in get_pests_list():
        print(pest.to_dict())