import formatting.helpers.family_ids as fam_id
import formatting.helpers.family_name as fam_name
import formatting.helpers.embarked as embarked
import formatting.helpers.fare as fare
import formatting.helpers.family_size as fam_size
import formatting.helpers.age as age
import formatting.helpers.sex as sex


def format_titanic_data(data, train_data):
    sex.extract(data)
    age.extract(data, train_data["Age"].median())
    embarked.extract(data)
    fam_size.extract(data)
    fare.extract(data)
    fam_id.extract(data)
    fam_name.extract(data)
    return data
