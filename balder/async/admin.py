from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from async.models import Product, ProductJson
from concurrency.admin import ConcurrentModelAdmin

TIME_FORMAT = "%d %b %Y %H:%M:%S"


class ProductAdmin(ConcurrentModelAdmin):
    fields = (
        'name',
        'updated',
        'exported',
        'version',
        "synced",
    )
    readonly_fields = (
        'product_json',
        'updated',
        'exported',
        "synced",
    )
    list_display = (
        'name',
        'updated',
        'exported',
        "synced",
    )

    def updated(self, obj):
        return obj.last_modified.strftime(TIME_FORMAT)

    def exported(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:async_productjson_change', args=(obj.product_json.id,)),
            obj.product_json.last_modified.strftime(TIME_FORMAT))
        )

    exported.short_description = "Last Exported"

    def synced(self, obj):
        return obj.last_modified < obj.product_json.last_modified

    synced.boolean = True


class ProductJsonAdmin(admin.ModelAdmin):
    fields = (
        'data',
        'updated',
        'related_product',
        'version'
    )
    readonly_fields = (
        'data',
        'updated',
        'related_product'
    )
    list_display = (
        'name',
        'updated',
    )

    def updated(self, obj):
        return obj.last_modified.strftime(TIME_FORMAT)

    def related_product(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:async_product_change', args=(obj.product.id,)),
            obj.product.name)
        )

    def name(self, obj):
        return obj.product.name

# register our models with the default admin view
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductJson, ProductJsonAdmin)
