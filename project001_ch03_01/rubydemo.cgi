######################
#simple ruby call
puts "hello\n\n"

######################
#regex
a = "8:25 AM"
x = /^(\d\d?):(\d\d)\s*([ap]m)$/i

a =~ x

puts "the time now is #{$1}H #{$2}M at the #{$3}" if $1 != nil
puts "the time pattern is not matched" if $1 == nil

######################
# Ruby classes demo
puts "\n\n"
puts 32.is_a? Integer
puts "32 is a #{32.class}"
puts "[1,2,3] is an #{[1,2,3].class}"
puts "{a: 1,b: 'a'} is a #{{a: 1,b: 'a'}.class}"
puts "'hello' is a #{'hello'.class}"
puts "3.2 is a #{3.2.class}"
puts "'a.class.class' is a #{'a'.class.class}"
puts "root class test for 'BasicObject': #{3.is_a? BasicObject}"

######################
# Ruby class hierarchy reflection
puts "\nint value class hierarchy:"
a_class = 3.class
pref = String.new

while (a_class != nil) do
	puts "#{pref}#{a_class}"
	a_class = a_class.superclass
	pref += "\t"
end


######################
# class reflection - listing methods
puts "\n\nreflecting on an integer:"

3.methods.each{ |m|
	print "#{m.to_sym}; "
}

######################
# class reflection - looking up methods
puts "\n\nreflecting on an integer methods origin:\n"
3.methods.sort.each {|m|
	puts  "#{m.to_sym} origin: #{3.method(m.to_sym)}"
} 

######################
# invoking methods using reflection
puts "abcdefg".gsub(/([af])/, "Q")
puts "abcdefg".send(:gsub, /([af])/, "Q")



