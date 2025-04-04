#ExpressionBuilders.py

from .app_state import Expressions


class ExpressionBuilders:
    @staticmethod
    def build_in_expression(field_name, values):
        """
        Build an expression to select features where the field's value is in a list.
        
        :param field_name: Name of the field to filter on.
        :param values: List of values to include in the filter.
        :return: A QGIS expression string.
        """
        if not values:
            return Expressions.clear
        # Construct the expression with correctly formatted quotes
        values_str = ",".join(f"'{v}'" for v in values)
        expression = f'"{field_name}" IN ({values_str})'
        print("Built In Expression:")
        print(expression)
        
        return expression

    @staticmethod
    def build_like_expression(field_name, pattern):
        """
        Build a LIKE expression for pattern matching.
        
        :param field_name: Name of the field to filter on.
        :param pattern: Pattern to match (e.g., 'A%', '%test%', etc.).
        :return: A QGIS expression string.
        """
        expression = f'"{field_name}" LIKE \'{pattern}\''
        print("Built LIKE Expression:")
        print(expression)
        return expression

    @staticmethod
    def build_between_expression(field_name, lower, upper):
        """
        Build a BETWEEN expression for filtering values between two bounds.
        
        :param field_name: Name of the field to filter on.
        :param lower: Lower bound of the value range.
        :param upper: Upper bound of the value range.
        :return: A QGIS expression string.
        """
        expression = f'"{field_name}" BETWEEN {lower} AND {upper}'
        print("Built BETWEEN Expression:")
        print(expression)
        return expression

    @staticmethod
    def combine_expressions(expressions, operator="AND"):
        """
        Combine multiple expressions with a specified logical operator.
        
        :param expressions: List of expression strings.
        :param operator: Logical operator to combine them (e.g., "AND", "OR").
        :return: A combined QGIS expression string.
        """
        # Filter out any empty expressions
        filtered_expr = [expr for expr in expressions if expr]
        if not filtered_expr:
            return Expressions.clear
        combined_expression = f" {operator} ".join(filtered_expr)
        print("Combined Expression:")
        print(combined_expression)
        return combined_expression

