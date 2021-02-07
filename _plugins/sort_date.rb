module SortDateFilter
  def sort_date(input)
    input.filter { |p| p.respond_to? :completed }.sort_by { |p| p.completed }
  end
end

Liquid::Template.register_filter(SortDateFilter)
