module SortDateFilter
  def sort_date(input)
    input.filter { |p|
      !p.data['completed'].nil?
    }.sort_by { |p|
      [p.data['completed'], p.data['title']]
    }
  end
end

Liquid::Template.register_filter(SortDateFilter)
