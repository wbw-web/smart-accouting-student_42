"""
数据分析模块
"""

class DataAnalyzer:
    def __init__(self, records):
        self.records = records
    
    def get_category_stats(self):
        """获取分类统计"""
        stats = {}
        for record in self.records:
            category = record['category']
            if category not in stats:
                stats[category] = {
                    'count': 0,
                    'total': 0,
                    'records': []
                }
            stats[category]['count'] += 1
            stats[category]['total'] += record['amount']
            stats[category]['records'].append(record)
        
        return stats
    
    def get_monthly_stats(self):
        """获取月度统计"""
        monthly = {}
        for record in self.records:
            month = record['timestamp'][:7]  # YYYY-MM
            if month not in monthly:
                monthly[month] = 0
            monthly[month] += record['amount']
        
        return monthly
