import csv
from xml.dom import minidom

from flask import Flask

app = Flask(__name__)
xml = r'C:/Users/rahsheth/Downloads/input.xml'


def execute():
    try:
        data_array = []
        voucher_number_array = []
        reference_array = []
        reference_type_array = []
        reference_date_array = []
        debtor_array = []
        reference_amount_array = []
        amount_array = []
        particulars_array = []
        voucher_type_array = []
        amount_verified_array = []


        file = minidom.parse(xml)
        vouchers = file.getElementsByTagName('VOUCHER')

        with open('xml_to_csv_file.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(["Date", "Vch No.", "Ref No", "Ref Type", "Ref Date", "Debtor", "Ref Amount", "Amount", "Particulars", "Vch Type", "Amount Verified"])
            for voucher in vouchers:
                date_obj = voucher.getElementsByTagName('DATE')
                if len(date_obj) > 0:
                    for a in date_obj:
                        date_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'date_text :: {date_text}')
                        data_array.append(date_text)
                        if date_text is not None:
                            break
                else:
                    data_array.append("Na")

                voucher_number = voucher.getElementsByTagName('VOUCHERNUMBER')
                if len(voucher_number) > 0:
                    for a in voucher_number:
                        voucher_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'voucher_text :: {voucher_text}')
                        voucher_number_array.append(voucher_text)
                        if voucher_text is not None:
                            break
                else:
                    voucher_number_array.append("Na")

                reference = voucher.getElementsByTagName('REFERENCE')
                if len(reference) > 0:
                    for a in reference:
                        reference_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'reference_text :: {reference_text}')
                        reference_array.append(reference_text)
                        if reference_text is not None:
                            break
                else:
                    reference_array.append("Na")

                reference_type = voucher.getElementsByTagName('BILLTYPE')
                if len(reference_type) > 0:
                    for a in reference_type:
                        reference_type_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'reference_type_text :: {reference_type_text}')
                        reference_type_array.append(reference_type_text)
                        if reference_type_text is not None:
                            break
                else:
                    reference_type_array.append("Na")

                reference_date = voucher.getElementsByTagName('REFERENCEDATE')
                if len(reference_date) > 0:
                    for a in reference_date:
                        reference_date_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'reference_date_text :: {reference_date_text}')
                        reference_date_array.append(reference_date_text)
                        if reference_date_text is not None:
                            break
                else:
                    reference_date_array.append("Na")

                debtor = voucher.getElementsByTagName('PARTYNAME')
                if len(debtor) > 0:
                    for a in debtor:
                        debtor_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'reference_date_text :: {debtor_text}')
                        debtor_array.append(debtor_text)
                        if debtor_text is not None:
                            break
                else:
                    debtor_array.append("Na")

                reference_amount = voucher.getElementsByTagName('AMOUNT')
                if len(reference_amount) > 0:
                    for a in reference_amount:
                        reference_amount_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'reference_date_text :: {reference_amount_text}')
                        reference_amount_array.append(reference_amount_text)
                        if reference_amount_text is not None:
                            break
                else:
                    reference_amount_array.append("Na")

                amount = voucher.getElementsByTagName('VATEXPAMOUNT')
                if len(amount) > 0:
                    for a in amount:
                        amount_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'amount_text :: {amount_text}')
                        amount_array.append(amount_text)
                        if amount_text is not None:
                            break
                else:
                    amount_array.append("Na")

                particulars = voucher.getElementsByTagName('LEDGERNAME')
                if len(particulars) > 0:
                    for a in particulars:
                        particulars_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'particulars_text :: {particulars_text}')
                        particulars_array.append(particulars_text)
                        if particulars_text is not None:
                            break
                else:
                    particulars_array.append("Na")

                voucher_type = voucher.getElementsByTagName('VOUCHERTYPENAME')
                if len(voucher_type) > 0:
                    for a in voucher_type:
                        voucher_type_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'voucher_type_text :: {voucher_type_text}')
                        voucher_type_array.append(voucher_type_text)
                        if voucher_type_text is not None:
                            break
                else:
                    voucher_type_array.append("Na")

                amount_verified = voucher.getElementsByTagName('ISVATDUTYPAID')
                if len(amount_verified) > 0:
                    for a in amount_verified:
                        amount_verified_text = a.childNodes[0].nodeValue if a is not None else 'NA'
                        print(f'amount_verified_text :: {amount_verified_text}')
                        amount_verified_array.append(amount_verified_text)
                        if amount_verified_text is not None:
                            break
                else:
                    amount_verified_array.append("Na")

                element = [sub[item] for item in range(len(amount_verified_array))
                    for sub in [data_array, voucher_number_array, reference_array, reference_type_array, reference_date_array, debtor_array, reference_amount_array, amount_array, particulars_array, voucher_type_array, amount_verified_array]]
                print(f'after element :: {element}')

                if len(element) > 0:
                    writer.writerow(element)

                if len(element) > 0:
                    print("Delete")
                    if len(element[0]) > 0:
                        data_array.remove(element[0])
                    if len(element[1]) > 0:
                        voucher_number_array.remove(element[1])
                    if len(element[2]) > 0:
                        reference_array.remove(element[2])
                    if len(element[3]) > 0:
                        reference_type_array.remove(element[3])
                    if len(element[4]) > 0:
                        reference_date_array.remove(element[4])
                    if len(element[5]) > 0:
                        debtor_array.remove(element[5])
                    if len(element[6]) > 0:
                        reference_amount_array.remove(element[6])
                    if len(element[7]) > 0:
                        amount_array.remove(element[7])
                    if len(element[8]) > 0:
                        particulars_array.remove(element[8])
                    if len(element[9]) > 0:
                        voucher_type_array.remove(element[9])
                    if len(element[10]) > 0:
                        amount_verified_array.remove(element[10])


        return "SUCCESS"

    except Exception as e:
        print(f"Error while converting xml to csv :: {e}")
        return "FAILED"


@app.route("/csv-generator-api")
def generate_dump():
    print("")
    print(">> xml to csv initiated.")

    result = execute()

    print("")
    print(">> xml to csv completed.")

    return result


if __name__ == "__main__":
    app.run()