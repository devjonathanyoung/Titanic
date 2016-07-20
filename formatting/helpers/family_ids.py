import operator

family_id_mapping = {}


def get_family_id(row):
    last_name = row["Name"].split(",")[0]
    family_id = "{0}{1}".format(last_name, row["FamilySize"])
    if family_id not in family_id_mapping:
        if len(family_id_mapping) == 0:
            current_id = 1
        else:
            # Get the maximum id from the mapping and add one to it if we don't have an id
            current_id = (max(family_id_mapping.items(), key=operator.itemgetter(1))[1] + 1)
        family_id_mapping[family_id] = current_id
    return family_id_mapping[family_id]


def extract(data):
    family_id_mapping = {}
    family_ids = data.apply(get_family_id, axis=1)
    family_ids[data["FamilySize"] < 3] = -1
    data["FamilyId"] = family_ids
