PRODUCT = [[1099 ,"SAR Playstation 4"],[3500 ,"SAR Hp zbook firefly g9"],[3330 ,"SAR xiaomi 17 pro"],[3070 ,"SAR Samsung refrigerator"],[1379 , "SAR samsung galaxy watch 8"] ]
TAX_RATE = 0.15
def calculate_total_price(price,tax_rate):

   total_price = price * (1 + tax_rate)
   return total_price

def run_backend_project():
    print("##اختر رقم المنتج:\n")

    for index, product in enumerate(PRODUCT):
        product_number = index + 1
        product_price = product[0]
        product_name = product[1]
        print(f"{product_number} - {product_name} (Price: {product_price})")

    while True:
        try:
            user_input = input("\nاكتب الرقم:")
            selected_number = int(user_input)
            selected_index = selected_number - 1

            if 0 <= selected_index < len(PRODUCT):
                break
            else:
                print(f"\nرقم المنتج غير صحيح. الرجاء إدخال رقم بين 1 و {len(PRODUCT)}.")
        except ValueError:
            print("\nإدخال غير صحيح. الرجاء إدخال رقم صحيح.")
    
    selected_product_price = PRODUCT[selected_index][0]
    selected_product_name = PRODUCT[selected_index][1]
    total_price_with_tax = calculate_total_price(selected_product_price,TAX_RATE)
    print(f"\n---")
    print(f"المنتج المختار: {selected_product_name}")
    print(f"سعر المنتج شامل الضريبة: {total_price_with_tax:.2f} SAR")
    print(f"---")

if __name__== "__main__":
    run_backend_project()


